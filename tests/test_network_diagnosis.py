
import unittest

from netson.diagnostics.ipv4 import diagnose_network

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


    def test_device_network_address(self):
        result = diagnose_network(
            "192.168.1.0",
            "192.168.1.1",
            "255.255.255.0"
        )

        self.assertEqual(result["status"], "error")

    def test_device_broadcast_address(self):
        result = diagnose_network(
            "192.168.1.255",
            "192.168.1.1",
            "255.255.255.0"
        )

        self.assertEqual(result["status"], "error")

    def test_gateway_network_address(self):
        result = diagnose_network(
            "192.168.1.100",
            "192.168.1.0",
            "255.255.255.0"
        )

        self.assertEqual(result["status"], "error")

    def test_gateway_broadcast_address(self):
        result = diagnose_network(
            "192.168.1.100",
            "192.168.1.255",
            "255.255.255.0"
        )

        self.assertEqual(result["status"], "error")

    def test_whitespace_in_input(self):
        result = diagnose_network(
            " 192.168.1.100 ",
            " 192.168.1.1 ",
            " 255.255.255.0 "
        )

        self.assertEqual(result["status"], "success")

    def test_cidr_notation(self):
        result = diagnose_network(
            "192.168.1.100",
            "192.168.1.1",
            "/24"
        )

        self.assertEqual(result["status"], "success")

    def test_valid_point_to_point_subnet(self):
        result = diagnose_network(
            "192.168.1.0",
            "192.168.1.1",
            "/31"
        )

        self.assertEqual(result["status"], "success")

    def test_single_address_subnet(self):
        result = diagnose_network(
            "192.168.1.100",
            "192.168.1.101",
            "/32"
        )

        self.assertEqual(result["status"], "warning")


    def test_device_and_gateway_same_address(self):
        result = diagnose_network(
            "192.168.1.100",
            "192.168.1.100",
            "255.255.255.0"
        )

        self.assertEqual(result["status"], "error")

    def test_invalid_cidr_prefix(self):
        result = diagnose_network(
            "192.168.1.100",
            "192.168.1.1",
            "/33"
        )

        self.assertEqual(result["status"], "error")

    def test_empty_subnet_mask(self):
        result = diagnose_network(
            "192.168.1.100",
            "192.168.1.1",
            ""
        )

        self.assertEqual(result["status"], "error")

    def test_same_address_in_point_to_point_subnet(self):
        result = diagnose_network(
            "192.168.1.0",
            "192.168.1.0",
            "/31"
        )

        self.assertEqual(result["status"], "error")


    def test_none_device_ip(self):
        result = diagnose_network(
            None,
            "192.168.1.1",
            "255.255.255.0"
        )

        self.assertEqual(result["status"], "error")
        self.assertEqual(
            result["problem"],
            "Invalid device IP address."
        )

    def test_non_string_gateway(self):
        result = diagnose_network(
            "192.168.1.100",
            12345,
            "255.255.255.0"
        )

        self.assertEqual(result["status"], "error")
        self.assertEqual(
            result["problem"],
            "Invalid gateway address."
        )

    def test_none_subnet_mask(self):
        result = diagnose_network(
            "192.168.1.100",
            "192.168.1.1",
            None
        )

        self.assertEqual(result["status"], "error")
        self.assertEqual(
            result["problem"],
            "Invalid subnet mask."
        )




if __name__ == "__main__":
    unittest.main()
