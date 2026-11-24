import json

CONFIG_FILE = "data/firewall_policies.json"


def load_firewall_config():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


def analyze_policy(policy):
    service = policy["service"].upper()
    action = policy["action"].lower()
    enabled = policy["enabled"]

    if service == "TELNET" and action == "allow" and enabled:
        return "CRITICAL: Enabled rule allows insecure Telnet"

    if service == "TELNET" and action == "deny":
        return "SECURE: Telnet traffic is denied"

    return "INFO: Rule reviewed"


def main():
    try:
        data = load_firewall_config()

        print("====================================")
        print(" FIREWALL POLICY ANALYZER")
        print("====================================")
        print("Firewall:", data["firewall"]["hostname"])

        for policy in data["policies"]:
            print("\nRule:", policy["name"])
            print(analyze_policy(policy))

    except FileNotFoundError:
        print("ERROR: Configuration file not found")

    except json.JSONDecodeError:
        print("ERROR: Invalid JSON configuration")

    except (KeyError, TypeError, AttributeError) as error:
        print("ERROR: Invalid configuration structure:", error)


if __name__ == "__main__":
    main()
