Firewall Implementation Simulator
Overview
The Firewall Implementation Simulator is a simple Python-based tool that simulates the behavior of a firewall by filtering network traffic based on pre-configured rules. The simulator checks incoming packets against the rules and logs any blocked traffic for further analysis. This project serves as a learning tool for those who want to understand how firewalls work in network security.

Features
Simulates Firewall Rules: Filters incoming network packets based on source IP, destination IP, port, and protocol.

Logging: Logs all blocked traffic to a file (blocked_traffic.log), making it easy to track potentially harmful packets.

Simple Rule Matching: Currently, the simulator matches packets based on pre-configured rules. The firewall can allow or block traffic depending on the rule.

Current Features
Basic Filtering: Filters packets based on the following parameters:

Source IP

Destination IP

Port

Protocol

Logging of Blocked Traffic: Every time a packet is blocked, it is logged in the blocked_traffic.log file with details like source, destination, and port.

Future Improvements
This is a simple project to simulate firewall functionality. Here are some planned improvements for future versions:

Real-time Traffic Monitoring: Track and log traffic in real-time.

Enhanced Logging: Add timestamps and further analysis of blocked packets.

User Interface: A more user-friendly interface to add, modify, or delete firewall rules easily.

Advanced Rule Matching: Support for more complex rules (e.g., matching ranges of IPs or port numbers).

Integration with Real Firewall Systems: Extend the project to work with actual firewall systems (using libraries like iptables).

Requirements
Before running the project, make sure you have the following installed:

Python 3.x or higher

Basic understanding of Python and networking concepts.

Installation
Clone this repository:

bash
Copier le code
git clone https://github.com/yourusername/firewall-simulator.git
cd firewall-simulator
Install any necessary dependencies (if any). Currently, no additional libraries are required for this basic version.

Run the simulator:

bash
Copier le code
python firewall_simulator.py
Usage
Firewall Rule Configuration:

The firewall checks packets against a set of pre-configured rules. You can modify the rules list in the firewall_simulator.py file to add your own rules.

Packet Simulation:

The packets list simulates network traffic. Each packet contains:

src_ip: Source IP address.

dest_ip: Destination IP address.

port: Port number.

protocol: Communication protocol (e.g., "TCP", "UDP").

Viewing Blocked Traffic:

After running the simulator, check the blocked_traffic.log file to view all blocked traffic.

Contributing
Contributions are welcome! If you’d like to improve the project, feel free to fork the repository, create a pull request, or open an issue if you encounter any bugs.

License
This project is licensed under the MIT License - see the LICENSE file for details.

