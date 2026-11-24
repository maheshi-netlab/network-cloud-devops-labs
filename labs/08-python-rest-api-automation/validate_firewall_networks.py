import json
import ipaddress

CONFIG_FILE = "data/firewall_policies.json"

try:
    with open(CONFIG_FILE, "r") as file:
        data = json.load(file)

    firewall = data["firewall"]
    policies = data["policies"]

    print("====================================")
    print(" FIREWALL NETWORK VALIDATION")
    print("====================================")

    try:
        management_ip = ipaddress.ip_address(
            firewall["management_ip"]
        )
        print("PASS: Management IP:", management_ip)
    except ValueError:
        print("FAIL: Invalid management IP")

    for policy in policies:
        print("\nRule:", policy["name"])

        for field in ["source", "destination"]:
            value = policy[field]

            if value.lower() == "any":
                print("PASS:", field, "is ANY")
                continue

            try:
                network = ipaddress.ip_network(
                    value, strict=False
                )
                print("PASS:", field, network)
            except ValueError:
                print("FAIL: Invalid", field, value)

except FileNotFoundError:
    print("ERROR: Configuration file not found")

except json.JSONDecodeError:
    print("ERROR: Invalid JSON configuration")

except (KeyError, TypeError) as error:
    print("ERROR: Invalid configuration structure:", error)
