import json

CONFIG_FILE = "data/firewall_policies.json"

try:
    with open(CONFIG_FILE, "r") as file:
        data = json.load(file)

    firewall = data["firewall"]
    policies = data["policies"]

    print("====================================")
    print(" FIREWALL SECURITY ANALYSIS")
    print("====================================")

    print("Firewall:", firewall["hostname"])

    for policy in policies:
        service = policy["service"].upper()
        action = policy["action"].lower()
        enabled = policy["enabled"]

        print("\nRule:", policy["name"])

        if service == "TELNET" and action == "allow" and enabled:
            print("CRITICAL: Enabled rule allows insecure Telnet")
        elif service == "TELNET" and action == "deny":
            print("SECURE: Telnet traffic is denied")
        else:
            print("INFO: Rule reviewed")

except FileNotFoundError:
    print("ERROR: Configuration file not found")

except json.JSONDecodeError:
    print("ERROR: Invalid JSON configuration")

except (KeyError, TypeError, AttributeError) as error:
    print("ERROR: Invalid configuration structure:", error)
