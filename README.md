# TCP Port Scanner

A simple TCP port scanner written in Python for learning networking, sockets, and basic cybersecurity concepts.

This project was built as part of my journey into ethical hacking and Python programming. The goal was not just to create a scanner, but to understand how TCP connections work internally and how network reconnaissance tools are built.

## Features

* Scan common TCP ports
* Scan custom TCP ports
* Detect common services
* Display open and closed ports
* Measure total scan time
* Clean, beginner-friendly code

## Requirements

* Python 3.x
* Git (optional, for cloning the repository)

## Installation

Clone the repository:

```bash
git clone https://github.com/atlasinfosec93-RBT/python-tcp_port_scanner.git
```

Navigate to the project folder:

```bash
cd python-tcp_port_scanner
```

Run the scanner:

```bash
python port_scanner.py
```

## Usage

1. Enter the target IP address.
2. Choose whether to scan the predefined common ports (`y`) or your own ports (`n`).
3. If you choose custom ports, enter them as a comma-separated list.

Example:

```text
Target IP: 192.168.1.1
Scan famous ports? (y/n): n
Enter ports to scan (comma-separated): 22,80,443
```

Example output:

```text
========================================
        TCP PORT SCANNER
      Made by @de4ault.93
========================================

[+] Port 22 is OPEN
    Service: ssh

[+] Port 80 is OPEN
    Service: http

[-] Port 25 is closed

Scan completed in 1.42 seconds.
```

## Technologies Used

* Python
* Socket Programming
* TCP Networking
* Git
* GitHub

## Disclaimer

This project is intended for educational purposes only. Only scan systems that you own or have explicit permission to test.

## Future Improvements

* Banner grabbing
* Threaded scanning
* Port range support
* Command-line arguments
* Export scan results
* Better error handling

## Author

**Fouad (@de4ault.93)**

Learning Python, networking, Linux, and ethical hacking one project at a time.
