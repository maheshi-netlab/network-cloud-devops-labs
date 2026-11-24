import logging

logging.basicConfig(
    filename="reports/security_automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Network security automation started")
logging.info("Firewall configuration loaded")
logging.warning("Security policy requires review")
logging.error("Example API error event")

print("Logging demonstration completed")
print("Log file: reports/security_automation.log")
