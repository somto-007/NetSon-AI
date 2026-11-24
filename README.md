# NetSon-AI

**A Python-Based IPv4 Network Diagnostic Tool**

## Overview

NetSon-AI is a Python-based networking project developed to identify common IPv4 network configuration problems.

The application accepts a device IP address, default gateway, and subnet mask or CIDR prefix. It validates the supplied configuration, calculates the device's network, and checks whether the gateway belongs to the same subnet.

It produces a structured diagnostic report containing a status, an identified problem, and a recommendation.

The project is currently focused on building a reliable diagnostic foundation that can later support additional networking tools and interfaces.

## Problem Statement

Incorrect IP addresses, subnet masks, and default gateway configurations can prevent devices from communicating correctly across networks.

NetSon-AI explores how common network configuration problems can be identified and explained through automated Python-based diagnostics.

## Current Features

- IPv4 address validation.
- Default gateway validation.
- Subnet mask and CIDR prefix validation.
- IPv4 network calculation.
- Gateway subnet membership checking.
- Detection of network and broadcast address assignments.
- Detection of identical device and gateway addresses.
- Structured diagnostic results.
- Terminal-based diagnostic reports.
- Automated unit testing with Python's `unittest` framework.

## Technologies Used

- **Python:** Main programming language.
- **ipaddress:** Python standard-library module for IPv4 address and network operations.
- **unittest:** Automated testing framework.
- **setuptools:** Python package building and installation.
- **Git and GitHub:** Version control and project hosting.

## Project Structure

```text
NetSon-AI/
├── src/
│   └── netson/
│       ├── __init__.py
│       ├── cli.py
│       └── diagnostics/
│           ├── __init__.py
│           └── ipv4.py
├── tests/
│   └── test_network_diagnosis.py
├── main.py
├── pyproject.toml
├── README.md
└── .gitignore
```

The diagnostic engine is separated from the command-line interface. This makes it possible to reuse the same diagnostic logic in future interfaces, including a web dashboard or desktop application.

## Installation and Usage

### Requirements

- Python 3.10 or later.
- Git (optional, for cloning the repository).

### Clone the repository

```bash
git clone https://github.com/somto-007/NetSon-AI.git
```

### Enter the project directory

```bash
cd NetSon-AI
```

### Install the project

```bash
python3 -m pip install -e .
```

### Run NetSon-AI

Using the installed command:

```bash
netson
```

Alternatively, use the project launcher:

```bash
python3 main.py
```

Enter the device IP address, default gateway, and subnet mask or CIDR prefix when prompted.

## Example

**Input**

| Parameter | Value |
|---|---|
| Device IP | `192.168.1.100` |
| Gateway | `192.168.2.1` |
| Subnet mask | `255.255.255.0` |

**Expected diagnostic result**

```text
=== NetSon-AI Diagnostic Report ===

Status: WARNING

Problem: Gateway is outside the device subnet.

Recommendation: Check the IP, subnet and routing configuration.
```

## Running Automated Tests

Run the following command from the project directory:

```bash
python3 -m unittest discover -s tests -v
```

The current test suite contains 20 tests covering valid configurations, invalid addresses, subnet boundaries, gateway validation, CIDR notation, and other edge cases.

## Current Limitations

NetSon-AI currently performs IPv4 configuration validation and subnet analysis.

It does not yet perform live connectivity tests, inspect network traffic, detect physical network faults, or automatically repair network configurations.

A successful result means that the implemented configuration checks have passed. It does not guarantee that the device can reach its gateway or access the internet.

Despite its name, NetSon-AI does not currently contain an AI or machine-learning model. Intelligent diagnostic assistance is a future development goal.

## Future Development

Planned improvements include:

- More comprehensive IPv4 diagnostics.
- Live gateway reachability testing.
- DNS and internet connectivity checks.
- Automated diagnostic report generation.
- Saving diagnostic results using a database.
- Device and network management capabilities.
- A graphical interface and web dashboard.
- Intelligent diagnostic assistance based on actual diagnostic results.
- Improved testing, documentation, and deployment.

## Project Status

**Current version:** 0.1.0

NetSon-AI is an actively developing personal networking project. Its current focus is establishing a modular, testable diagnostic foundation before expanding into more advanced networking capabilities.

## Author

**Somtochukwu Onwuma**

GitHub: https://github.com/somto-007