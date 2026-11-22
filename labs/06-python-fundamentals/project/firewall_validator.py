import json
import sys
import ipaddress

CONFIG_FILE = "labs/06-python-fundamentals/project/firewall.json"

def load_firewall_config(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("FAIL: Configuration file not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print("FAIL: Invalid JSON configuration")
        sys.exit(1)

def validate_hostname(hostname):
    if hostname:
        print("PASS: Hostname is configured")
        return True
    print("FAIL: Hostname is missing")
    return False

def validate_management_ip(ip):
    try:
        ipaddress.ip_address(ip)
        print("PASS: Management IP is valid")
        return True
    except ValueError:
        print("FAIL: Invalid management IP")
        return False

def validate_services(services):
    required_services = ["SSH", "HTTPS", "DNS"]
    failures = 0

    for service in required_services:
        if service in services:
            print("PASS:", service, "is configured")
        else:
            print("FAIL:", service, "is missing")
            failures += 1

    return failures == 0

config = load_firewall_config(CONFIG_FILE)

print("Firewall Configuration Validation")
print("==================================")

results = []

results.append(validate_hostname(config.get("hostname", "")))
results.append(validate_management_ip(config.get("management_ip", "")))
results.append(validate_services(config.get("allowed_services", [])))

if all(results):
    print("\nVALIDATION SUCCESSFUL")
    sys.exit(0)
else:
    print("\nVALIDATION FAILED")
    sys.exit(1)
