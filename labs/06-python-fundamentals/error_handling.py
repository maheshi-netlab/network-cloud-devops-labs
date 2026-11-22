import json

config_file = "labs/06-python-fundamentals/missing-config.json"

try:
    with open(config_file, "r") as file:
        config = json.load(file)

    print("Configuration loaded successfully")

except FileNotFoundError:
    print("ERROR: Firewall configuration file not found")

except json.JSONDecodeError:
    print("ERROR: Invalid JSON configuration")

print("Firewall automation continues")
