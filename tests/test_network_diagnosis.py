
import unittest

from main import diagnose_network


class TestNetworkDiagnosis(unittest.TestCase):

    def test_valid_configuration(self):
        result = diagnose_network(
            "192.168.1.100",
            "192.168.1.1",
            "255.255.255.0"
        )

        self.assertEqual(result["status"], "success")

    def test_gateway_outside_subnet(self):
        result = diagnose_network(
            "192.168.1.100",
            "192.168.2.1",
            "255.255.255.0"
        )

        self.assertEqual(result["status"], "warning")

    def test_invalid_device_ip(self):
        result = diagnose_network(
            "999.168.1.100",
            "192.168.1.1",
            "255.255.255.0"
        )

        self.assertEqual(result["status"], "error")
        self.assertEqual(
            result["problem"],
            "Invalid device IP address."
        )

    def test_invalid_gateway(self):
        result = diagnose_network(
            "192.168.1.100",
            "999.168.1.1",
            "255.255.255.0"
        )

        self.assertEqual(result["status"], "error")

    def test_invalid_subnet_mask(self):
        result = diagnose_network(
            "192.168.1.100",
            "192.168.1.1",
            "255.0.255.0"
        )

        self.assertEqual(result["status"], "error")


if __name__ == "__main__":
    unittest.main()
