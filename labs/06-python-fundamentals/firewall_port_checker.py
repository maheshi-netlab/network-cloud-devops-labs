firewall_enabled = True

allowed_ports = [22, 443, 53]

destination_ports = [22, 443, 53, 80, 8080]

print("Firewall Port Validation")
print("========================")

for port in destination_ports:

    if firewall_enabled and port in allowed_ports:
        print("PASS:", port, "is permitted")
    else:
        print("BLOCK:", port, "is not permitted")
