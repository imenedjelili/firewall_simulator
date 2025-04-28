# Firewall Implementation Simulator

## Overview

The **Firewall Implementation Simulator** is a simple Python-based tool that simulates the behavior of a firewall by filtering network traffic based on pre-configured rules. The simulator checks incoming packets against the rules and logs any blocked traffic for further analysis. This project serves as a learning tool for those who want to understand how firewalls work in network security.

## Features

- **Simulates Firewall Rules**: Filters incoming network packets based on **source IP**, **destination IP**, **port**, and **protocol**.
- **Logging**: Logs all blocked traffic to a file (`blocked_traffic.log`), making it easy to track potentially harmful packets.
- **Simple Rule Matching**: Currently, the simulator matches packets based on pre-configured rules. The firewall can **allow** or **block** traffic depending on the rule.

## Current Features

- **Basic Filtering**: Filters packets based on the following parameters:
  - **Source IP**
  - **Destination IP**
  - **Port**
  - **Protocol**
- **Logging of Blocked Traffic**: Every time a packet is blocked, it is logged in the `blocked_traffic.log` file with details like source, destination, and port.

## Future Improvements

This is a simple project to simulate firewall functionality. Here are some **planned improvements** for future versions:

- **Real-time Traffic Monitoring**: Track and log traffic in real-time.
- **Enhanced Logging**: Add timestamps and further analysis of blocked packets.
- **User Interface**: A more user-friendly interface to add, modify, or delete firewall rules easily.
- **Advanced Rule Matching**: Support for more complex rules (e.g., matching ranges of IPs or port numbers).
- **Integration with Real Firewall Systems**: Extend the project to work with actual firewall systems (using libraries like `iptables`).

## Requirements

Before running the project, make sure you have the following installed:

- **Python 3.x** or higher
- Basic understanding of **Python** and **networking concepts**.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/imenedjelili/firewall_simulator.git
   cd firewall-simulator
