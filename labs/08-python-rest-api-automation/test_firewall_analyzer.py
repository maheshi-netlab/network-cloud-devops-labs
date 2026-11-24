import unittest

from integrated_security_analyzer import analyze_policies


class TestFirewallAnalyzer(unittest.TestCase):

    def test_telnet_allow_is_critical(self):
        policies = [{
            "name": "Allow-Telnet",
            "service": "TELNET",
            "action": "allow",
            "enabled": True
        }]

        findings = analyze_policies(policies)

        self.assertEqual(
            findings[0]["severity"],
            "CRITICAL"
        )

    def test_telnet_deny_is_secure(self):
        policies = [{
            "name": "Block-Telnet",
            "service": "TELNET",
            "action": "deny",
            "enabled": True
        }]

        findings = analyze_policies(policies)

        self.assertEqual(
            findings[0]["severity"],
            "SECURE"
        )

    def test_https_is_informational(self):
        policies = [{
            "name": "Allow-HTTPS",
            "service": "HTTPS",
            "action": "allow",
            "enabled": True
        }]

        findings = analyze_policies(policies)

        self.assertEqual(
            findings[0]["severity"],
            "INFO"
        )


if __name__ == "__main__":
    unittest.main()
