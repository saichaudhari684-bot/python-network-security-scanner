# Python Network Security Scanner

A lightweight, multithreaded TCP port scanner developed in Python to practice network reconnaissance, socket programming, and fundamental cybersecurity concepts.

## Overview

This tool scans a specified range of TCP ports on an authorized target and identifies open ports. It also attempts to identify commonly associated services and generates a text-based scan report.

The project was developed as a hands-on cybersecurity learning project to understand how port scanning and basic network reconnaissance work.

## Features

- TCP port scanning
- Multithreaded scanning using ThreadPoolExecutor
- Configurable port range
- Configurable number of scanning threads
- Common service identification
- Input validation
- Scan duration measurement
- Automatic scan report generation
- Clean command-line interface

## Technologies

- Python 3
- Socket Programming
- TCP/IP Networking
- Concurrent Programming
- ThreadPoolExecutor
- Python Standard Library

## Project Structure

python-network-security-scanner/
│
├── scanner.py
├── README.md
├── requirements.txt
└── .gitignore

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/saichaudhari684-bot/python-network-security-scanner.git
