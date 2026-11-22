def validate_firewall_port(port, allowed_ports):

    if port in allowed_ports:
        print("PASS:", port, "is permitted")
    else:
        print("BLOCK:", port, "is not permitted")


allowed_ports = [22, 443, 53]

print("Firewall Function Validation")
print("=============================")

validate_firewall_port(22, allowed_ports)
validate_firewall_port(443, allowed_ports)
validate_firewall_port(80, allowed_ports)
validate_firewall_port(8080, allowed_ports)
