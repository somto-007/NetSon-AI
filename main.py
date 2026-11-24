
import ipaddress


def validate_ip(ip_address):
    try:
        return ipaddress.IPv4Address(ip_address)
    except ipaddress.AddressValueError:
        return None


def diagnose_network(ip_address, gateway, subnet_mask):

    ip = validate_ip(ip_address)
    gw = validate_ip(gateway)

    if ip is None:
        return {
            "status": "error",
            "problem": "Invalid device IP address.",
            "recommendation": "Check the device IP address."
        }

    if gw is None:
        return {
            "status": "error",
            "problem": "Invalid gateway address.",
            "recommendation": "Check the default gateway address."
        }

    try:
        network = ipaddress.IPv4Network(
            f"{ip}/{subnet_mask}",
            strict=False
        )
    except (ipaddress.AddressValueError,
            ipaddress.NetmaskValueError):
        return {
            "status": "error",
            "problem": "Invalid subnet mask.",
            "recommendation": "Enter a valid IPv4 subnet mask."
        }

    if gw not in network:
        return {
            "status": "warning",
            "problem": "Gateway is outside the device subnet.",
            "recommendation": "Check the IP and subnet settings."
        }

    return {
        "status": "success",
        "problem": "No subnet configuration issue detected.",
        "recommendation": "Next, test connectivity to the gateway."
    }


def display_report(result):

    print("\n=== NetSon-AI Diagnostic Report ===")
    print("Status:", result["status"].upper())
    print("Problem:", result["problem"])
    print("Recommendation:", result["recommendation"])


def main():

    print("Welcome to NetSon-AI!")

    ip = input("Enter device IP address: ")
    gateway = input("Enter default gateway: ")
    mask = input("Enter subnet mask: ")

    result = diagnose_network(ip, gateway, mask)

    display_report(result)


if __name__ == "__main__":
    main()
