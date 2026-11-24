import json

CONFIG_FILE = "data/firewall_policies.json"
REPORT_FILE = "reports/firewall_security_report.txt"


def load_config():
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


def generate_report(data):
    critical_count = 0
    secure_count = 0
    report_lines = []

    report_lines.append("FIREWALL SECURITY REPORT")
    report_lines.append("========================")
    report_lines.append("Firewall: " + data["firewall"]["hostname"])
    report_lines.append("")

    for policy in data["policies"]:
        finding = analyze_policy(policy)

        report_lines.append("Rule: " + policy["name"])
        report_lines.append(finding)
        report_lines.append("")

        if finding.startswith("CRITICAL"):
            critical_count += 1

        if finding.startswith("SECURE"):
            secure_count += 1

    report_lines.append("SUMMARY")
    report_lines.append("-------")
    report_lines.append("Total rules: " + str(len(data["policies"])))
    report_lines.append("Critical findings: " + str(critical_count))
    report_lines.append("Secure rules: " + str(secure_count))

    with open(REPORT_FILE, "w") as file:
        file.write("\n".join(report_lines))

    print("Report generated:", REPORT_FILE)
    print("Critical findings:", critical_count)
    print("Secure rules:", secure_count)


def main():
    try:
        data = load_config()
        generate_report(data)

    except FileNotFoundError:
        print("ERROR: Configuration or report directory not found")

    except json.JSONDecodeError:
        print("ERROR: Invalid JSON configuration")

    except (KeyError, TypeError, AttributeError) as error:
        print("ERROR: Invalid configuration structure:", error)


if __name__ == "__main__":
    main()
