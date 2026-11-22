firewall_enabled = True
destination_port = 8080

print("Firewall Policy Evaluation")
print("===========================")

if firewall_enabled == True:
    print("Firewall Status: ENABLED")

    if destination_port == 443:
        print("PASS: HTTPS traffic is permitted")
    elif destination_port == 22:
        print("PASS: SSH traffic is permitted")
    else:
        print("BLOCK: Port is not permitted")

else:
    print("BLOCK: Firewall is disabled")
