import json
import sys

config_file = "labs/05-json-fundamentals/network-config.json"

with open(config_file, "r") as file:
    config = json.load(file)

required_services = ["SSH", "HTTPS", "DNS"]
allowed_services = config["allowed_services"]

failures = 0

print("Firewall Service Validation")
print("============================")

for service in required_services:
    if service in allowed_services:
        print("PASS:", service, "is allowed")
    else:
        print("FAIL:", service, "is missing")
        failures += 1

if failures > 0:
    print("VALIDATION FAILED")
    sys.exit(1)

print("VALIDATION SUCCESSFUL")
sys.exit(0)
