# Simulate some network traffic (fake packets)
packets = [
    {"src_ip" : "192.168.1.1", "dest_ip": "192.168.1.100", "port": 80, "protocol": "HTTP"},
    {"src_ip" : "192.168.1.2", "dest_ip": "192.168.1.100", "port": 22, "protocol": "SSH"},
    {"src_ip" : "192.168.1.3", "dest_ip": "192.168.1.50", "port": 80, "protocol": "HTTP"},
    {"src_ip" : "192.168.1.4", "dest_ip": "192.168.1.50", "port": 80, "protocol": "HTTP"},
    {"src_ip" : "192.168.1.5", "dest_ip": "192.168.1.10", "port": 23, "protocol": "Telnet"},
    {"src_ip" : "192.168.1.6", "dest_ip": "192.168.1.70", "port": 23, "protocol": "Telnet"}
]

# Defineing the firewall rules 
firewall_rules = [
    {"action": "ALLOW", "src_ip": "192.168.1.2", "dest_ip": "192.168.1.100", "port": 80, "protocol": "HTTP"},
    {"action": "BLOCK", "src_ip" : "192.168.1.5", "dest_ip": "192.168.1.10", "port": 23, "protocol": "Telnet"},
    {"action": "BLOCK", "src_ip" : "192.168.1.6", "dest_ip": "192.168.1.70", "port": 23, "protocol": "Telnet"},

]

# Firewall Logic
def apply_firewall_rules(packets, rules):
 with open("blocked_traffic.log", "a") as log_file:
    for packet in packets:
        allowed = False # Assume packet is blocked by default
        for rule in rules:
            if (packet["src_ip"] == rule["src_ip"] and
                packet["dest_ip"] == rule["dest_ip"] and
                packet["port"] == rule["port"] and
                packet["protocol"] == rule["protocol"]):
                
                if rule["action"] == "ALLOW":
                    allowed = True
                    print(f"Packet from {packet['src_ip']} to {packet['dest_ip']} on port {packet['port']} allowed.")
                elif rule["action"] == "BLOCK":
                    allowed = False
                    print(f"Packet from {packet['src_ip']} to {packet['dest_ip']} on port {packet['port']} blocked.")
                    # Log the blocked packet to the file
                    log_file.write(f"Blocked packet from {packet['src_ip']} to {packet['dest_ip']} on port {packet['port']}\n")
                break # Exit the loop if a matching rule is found
        # If no rule matches, the packet is considered blocked
        if not allowed:
            print(f"Packet from {packet['src_ip']} to {packet['dest_ip']} on port {packet['port']} blocked by default.")
            log_file.write(f"Blocked packet from {packet['src_ip']} to {packet['dest_ip']} on port {packet['port']}\n")

# Apply Firewall rules to the previous defined packets
apply_firewall_rules(packets, firewall_rules)