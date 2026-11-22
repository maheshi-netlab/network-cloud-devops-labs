import json

config_file = "labs/05-json-fundamentals/network-config.json"

with open(config_file, "r") as file:
    config = json.load(file)

print("Hostname:", config["hostname"])
print("Primary DNS:", config["dns"]["primary"])

print("\nAllowed Firewall Services:")

for service in config["allowed_services"]:
    print("Permitted Service:", service)
