import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime


COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "Microsoft RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP Proxy",
}


def detect_service(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)

            if sock.connect_ex((target, port)) == 0:
                try:
                    service = socket.getservbyport(port, "tcp")
                except OSError:
                    service = COMMON_SERVICES.get(port, "Unknown")

                return port, service

    except (socket.error, OSError):
        pass

    return None


def scan_port(target, port):
    result = detect_service(target, port)

    if result:
        port, service = result
        return port, service

    return None


def save_report(target, start_port, end_port, open_ports, duration):
    filename = "scan_report.txt"

    with open(filename, "w", encoding="utf-8") as report:
        report.write("=" * 60 + "\n")
        report.write("PYTHON NETWORK SECURITY SCANNER\n")
        report.write("=" * 60 + "\n\n")

        report.write(f"Target       : {target}\n")
        report.write(f"Port Range   : {start_port}-{end_port}\n")
        report.write(f"Open Ports   : {len(open_ports)}\n")
        report.write(f"Scan Duration: {duration}\n\n")

        report.write("OPEN PORTS\n")
        report.write("-" * 60 + "\n")

        for port, service in open_ports:
            report.write(f"{port:<8} {service}\n")

    return filename


def main():
    print("=" * 60)
    print("             PYTHON NETWORK SECURITY SCANNER")
    print("=" * 60)

    target = input("Enter target IP/hostname: ").strip()

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\nError: Unable to resolve target.")
        return

    try:
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))
        threads = int(input("Number of threads (default 100): ") or 100)
    except ValueError:
        print("\nError: Please enter valid numbers.")
        return

    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
        print("Error: Ports must be between 1 and 65535.")
        return

    if start_port > end_port:
        print("Error: Start port cannot be greater than end port.")
        return

    if not 1 <= threads <= 500:
        print("Error: Threads must be between 1 and 500.")
        return

    print("\n" + "-" * 60)
    print(f"Target       : {target}")
    print(f"IP Address   : {target_ip}")
    print(f"Port Range   : {start_port}-{end_port}")
    print(f"Threads      : {threads}")
    print("-" * 60)
    print("Scanning...\n")

    start_time = datetime.now()
    open_ports = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [
            executor.submit(scan_port, target_ip, port)
            for port in range(start_port, end_port + 1)
        ]

        for future in as_completed(futures):
            result = future.result()

            if result:
                open_ports.append(result)
                port, service = result
                print(f"[OPEN]  Port {port:<5} {service}")

    open_ports.sort()

    duration = datetime.now() - start_time

    print("\n" + "=" * 60)
    print("                  SCAN SUMMARY")
    print("=" * 60)
    print(f"Target          : {target}")
    print(f"Ports scanned   : {end_port - start_port + 1}")
    print(f"Open ports      : {len(open_ports)}")
    print(f"Scan duration   : {duration}")

    if open_ports:
        print("\nOpen Ports:")
        for port, service in open_ports:
            print(f"  {port:<6} {service}")
    else:
        print("\nNo open ports found.")

    report = save_report(
        target,
        start_port,
        end_port,
        open_ports,
        duration
    )

    print(f"\nReport saved to: {report}")
    print("=" * 60)


if __name__ == "__main__":
    main()