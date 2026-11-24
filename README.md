# NetSon-AI

**A Python-Based IPv4 Network Diagnostic Tool**

## Overview

NetSon-AI is a beginner-built networking project developed in Python to identify common IPv4 network configuration problems.

The application accepts a device IP address, default gateway and subnet mask. It validates the supplied configuration, calculates the device's network and checks whether the gateway belongs to the same subnet.

It then produces a structured diagnostic result containing a status, an identified problem and a recommendation.

## Problem Statement

Incorrect IP addresses, subnet masks and default gateway configurations can prevent devices from communicating correctly across networks.

NetSon-AI was developed as a practical project to explore how basic network configuration checks can be automated using Python.

## Features

- IPv4 address validation.
- Default gateway validation.
- Subnet mask validation.
- IPv4 network calculation.
- Gateway subnet membership checking.
- Structured diagnostic results.
- Diagnostic report displayed in the terminal.
- Automated tests using Python's `unittest` framework.

## Technologies Used

- **Python:** Main programming language.
- **ipaddress:** Python standard-library module for IPv4 address and network operations.
- **unittest:** Python standard-library testing framework.
- **Git and GitHub:** Version control and project hosting.

## How It Works

1. The user enters a device IP address, default gateway and subnet mask.
2. The application validates the IP addresses.
3. It calculates the device's network using the supplied subnet mask.
4. It checks whether the gateway belongs to the calculated subnet.
5. It returns a diagnostic status and recommendation.
6. The report is displayed in the terminal.

## Example

**Input**

| Parameter | Value |
|---|---|
| Device IP | `192.168.1.100` |
| Gateway | `192.168.2.1` |
| Subnet mask | `255.255.255.0` |

**Expected diagnostic result**

```text
Status: WARNING
Problem: Gateway is outside the device subnet.
Recommendation: Check the IP and subnet settings.
```

## Installation and Usage

### Requirements

- Python 3.10 or later.
- Git (optional, for cloning the repository).

No external Python packages are required.

### Clone the repository

```bash
git clone https://github.com/somto-007/NetSon-AI.git
```

### Enter the project directory

```bash
cd NetSon-AI
```

### Run the application

```bash
python3 main.py
```

Enter the requested network configuration when prompted.

## Running Automated Tests

Run the following command from the project directory:

```bash
python3 -m unittest discover -s tests -v
```

The tests cover:

- Valid network configuration.
- Gateway outside the device subnet.
- Invalid device IP address.
- Invalid gateway address.
- Invalid subnet mask.

## Current Limitations

NetSon-AI currently performs configuration validation and subnet analysis.

It does not yet perform live connectivity tests, detect physical network faults, inspect network traffic or automatically repair network configurations.

A successful result means that the checks implemented by the application have passed; it does not guarantee that the device has internet connectivity.

## Future Development

Planned improvements include:

- More comprehensive IPv4 configuration checks.
- Automated diagnostic report generation.
- Saving diagnostic results.
- A graphical user interface.
- Live gateway connectivity testing.
- Expanded diagnostic rules and recommendations.
- Further networking and troubleshooting capabilities.

## Project