# Network Recon Tool

A Python-based network reconnaissance tool designed to perform basic host discovery and service enumeration tasks. This project is being built as part of a structured Python learning roadmap focused on networking and red team fundamentals.

---

## Project Goal

The goal of this project is to learn Python by building a practical networking tool that can:

* Resolve domain names to IP addresses
* Check host reachability
* Scan common TCP ports
* Perform service banner grabbing
* Generate simple reports

This project is intended for educational purposes and should only be used against systems that you own or have explicit permission to test.

---

## Features

### DNS Resolution

Convert a domain name into its corresponding IP address.

**Example**

Input:
google.com

Output:
142.250.xxx.xxx

---

### Host Reachability Check

Determine whether a target host is reachable.

**Example**

Input:
scanme.nmap.org

Output:
Host Reachable

---

### Port Scanning

Identify open TCP ports on a target host.

**Example**

Output:
22 Open
80 Open
443 Open

---

### Banner Grabbing

Attempt to retrieve service information from open ports.

**Example**

Output:
OpenSSH_9.x
Apache/2.4.x

---

### Report Generation

Save scan results for future analysis.

Supported formats:

* TXT
* JSON

---

## Project Structure

network_recon_tool/

├── main.py

├── dns_lookup.py

├── scanner.py

├── banner_grabber.py

├── reporter.py

├── results/

└── README.md

---

## Learning Objectives

This project is designed to strengthen understanding of:

### Python

* Functions
* Modules
* Exception Handling
* File Operations
* JSON Processing
* Command-Line Arguments

### Networking

* DNS Resolution
* TCP/IP
* Ports and Services
* Sockets
* Service Enumeration

### Security

* Reconnaissance
* Host Discovery
* Service Identification
* Basic Enumeration

---

## Planned Workflow

1. Accept target input from the user.
2. Resolve the target hostname.
3. Verify host availability.
4. Scan selected ports.
5. Collect service banners.
6. Save results to a report.
7. Display summary to the user.

---

## Example Execution Flow

User Input
↓
DNS Resolution
↓
Host Reachability
↓
Port Scan
↓
Banner Grabbing
↓
Report Generation

---

## Future Improvements

* Multi-threaded scanning
* CIDR range scanning
* Service fingerprinting
* Export to CSV
* Scan profiles
* Interactive CLI dashboard

---

## Author

Neetigya Maurya

Project Type: Python Networking & Red Team Learning Project

Status: In Development
