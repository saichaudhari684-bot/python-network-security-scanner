\# Python Network Security Scanner



A lightweight, multithreaded TCP port scanner developed in Python to practice network reconnaissance, socket programming, and fundamental cybersecurity concepts.



\## Overview



This tool scans a specified range of TCP ports on an authorized target and identifies open ports. It also attempts to identify commonly associated services and generates a text-based scan report.



The project was developed as a hands-on cybersecurity learning project to understand how port scanning and basic network reconnaissance work.



\## Features



\- TCP port scanning

\- Multithreaded scanning using ThreadPoolExecutor

\- Configurable port range

\- Configurable number of scanning threads

\- Common service identification

\- Input validation

\- Scan duration measurement

\- Automatic scan report generation

\- Clean command-line interface



\## Technologies



\- Python 3

\- Socket Programming

\- TCP/IP Networking

\- Concurrent Programming

\- ThreadPoolExecutor

\- Python Standard Library



\## Project Structure



python-network-security-scanner/

├── scanner.py

├── README.md

├── requirements.txt

└── .gitignore



\## Installation



\### 1. Clone the repository



&#x20;   git clone https://github.com/saichaudhari684-bot/python-network-security-scanner.git



\### 2. Navigate to the project directory



&#x20;   cd python-network-security-scanner



\### 3. Run the scanner



&#x20;   python scanner.py



No external Python packages are required.



\## Usage



When the program starts, enter:



\- Target IP address or hostname

\- Starting port

\- Ending port

\- Number of scanning threads



\### Example



&#x20;   Enter target IP/hostname: 127.0.0.1

&#x20;   Start port: 1

&#x20;   End port: 1000

&#x20;   Number of threads (default 100): 100



\## Example Output



&#x20;   \[OPEN]  Port 135   epmap

&#x20;   \[OPEN]  Port 445   microsoft-ds



&#x20;   ============================================================

&#x20;                     SCAN SUMMARY

&#x20;   ============================================================

&#x20;   Target          : 127.0.0.1

&#x20;   Ports scanned   : 1000

&#x20;   Open ports      : 2

&#x20;   Scan duration   : 0:00:05



The actual results will vary depending on the services running on the target system.



\## How It Works



1\. Resolves the target hostname to an IP address.

2\. Creates TCP socket connections for the selected ports.

3\. Uses multiple worker threads to perform scans concurrently.

4\. Identifies ports accepting TCP connections.

5\. Attempts to associate open ports with common services.

6\. Displays the results in the terminal.

7\. Saves the scan results to scan\_report.txt.



\## Learning Objectives



This project helped me gain practical experience with:



\- TCP/IP networking

\- Python socket programming

\- Port scanning concepts

\- Network reconnaissance

\- Concurrent programming

\- Basic security testing

\- Command-line application development



\## Future Improvements



Planned improvements include:



\- Service banner detection

\- CSV and JSON report generation

\- Improved service identification

\- Scan progress indicator

\- Custom timeout configuration

\- More detailed scan results



\## Ethical Use



This tool is intended for educational and authorized security testing only.



Use it only against systems that you own or have explicit permission to test. Unauthorized scanning of systems or networks may violate laws, policies, or terms of service.



\## Author



Sai Chaudhari



Cybersecurity Student | VAPT | Ethical Hacking | Network Security | SOC



GitHub: https://github.com/saichaudhari684-bot

