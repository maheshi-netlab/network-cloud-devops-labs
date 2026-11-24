import os
import json
import requests
import logging
from datetime import datetime

API_URL = "https://jsonplaceholder.typicode.com/posts/1"
CONFIG_FILE = "data/firewall_policies.json"
REPORT_FILE = "reports/integrated_security_report.txt"
LOG_FILE = "reports/security_automation.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def check_api_connectivity():
    token = os.getenv("FIREWALL_API_TOKEN")

    if not token:
        logging.warning("API token not configured")
        return "NOT CONFIGURED"

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + token
    }

    try:
        response = requests.get(
            API_URL,
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:
            logging.info("Test API connectivity successful")
            return "SUCCESS (HTTP 200)"

        logging.error(
            "Test API returned HTTP %s",
            response.status_code
        )
        return "FAILED (HTTP " + str(response.status_code) + ")"

    except requests.exceptions.RequestException as error:
        logging.error("API connection error: %s", error)
        return "CONNECTION ERROR"


def load_firewall_config():
    logging.info("Loading firewall configuration")

    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


def analyze_policies(policies):
    findings = []

    for policy in policies:
        service = policy["service"].upper()
        action = policy["action"].lower()
        enabled = policy["enabled"]

        if service == "TELNET" and action == "allow" and enabled:
            severity = "CRITICAL"
            message = "Enabled rule allows insecure Telnet"
            logging.critical(
                "Insecure Telnet rule detected: %s",
                policy["name"]
            )

        elif service == "TELNET" and action == "deny":
            severity = "SECURE"
            message = "Telnet traffic is denied"
            logging.info("Telnet deny rule verified")

        else:
            severity = "INFO"
            message = "Rule reviewed"
            logging.info("Policy reviewed: %s", policy["name"])

        findings.append({
            "rule": policy["name"],
            "severity": severity,
            "message": message
        })

    return findings


def generate_report(firewall, findings, api_status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    critical = 0
    secure = 0
    info = 0

    lines = [
        "INTEGRATED NETWORK SECURITY REPORT",
        "==================================",
        "Generated: " + timestamp,
        "Firewall: " + firewall["hostname"],
        "Management IP: " + firewall["management_ip"],
        "Vendor: " + firewall["vendor"],
        "Environment: " + firewall["environment"],
        "Test API Connectivity: " + api_status,
        "",
        "FIREWALL POLICY ANALYSIS",
        "------------------------"
    ]

    for finding in findings:
        lines.append("Rule: " + finding["rule"])
        lines.append("Severity: " + finding["severity"])
        lines.append("Finding: " + finding["message"])
        lines.append("")

        if finding["severity"] == "CRITICAL":
            critical += 1
        elif finding["severity"] == "SECURE":
            secure += 1
        else:
            info += 1

    lines.extend([
        "SUMMARY",
        "-------",
        "Total rules: " + str(len(findings)),
        "Critical findings: " + str(critical),
        "Secure rules: " + str(secure),
        "Informational rules: " + str(info)
    ])

    with open(REPORT_FILE, "w") as file:
        file.write("\n".join(lines))

    logging.info("Security report generated: %s", REPORT_FILE)
    logging.info(
        "Analysis completed: critical=%s secure=%s info=%s",
        critical, secure, info
    )

    print("Report generated:", REPORT_FILE)
    print("Critical findings:", critical)
    print("Secure rules:", secure)
    print("Informational rules:", info)


def main():
    try:
        print("====================================")
        print(" INTEGRATED SECURITY ANALYZER")
        print("====================================")

        logging.info("Security analyzer started")

        api_status = check_api_connectivity()
        print("Test API status:", api_status)

        data = load_firewall_config()
        findings = analyze_policies(data["policies"])

        generate_report(
            data["firewall"],
            findings,
            api_status
        )

        logging.info("Security analyzer completed")

    except FileNotFoundError:
        logging.exception("Required configuration or directory missing")
        print("ERROR: Required configuration or directory missing")

    except json.JSONDecodeError:
        logging.exception("Invalid JSON configuration")
        print("ERROR: Invalid JSON configuration")

    except (KeyError, TypeError, AttributeError):
        logging.exception("Invalid configuration structure")
        print("ERROR: Invalid configuration structure")


if __name__ == "__main__":
    main()
