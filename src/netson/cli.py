
from netson.diagnostics.ipv4 import diagnose_network


def display_report(result):
    print("\n=== NetSon-AI Diagnostic Report ===")
    print("Status:", result["status"].upper())
    print("Problem:", result["problem"])
    print("Recommendation:", result["recommendation"])


def main():
    print("Welcome to NetSon-AI!")

    ip = input("Enter device IP address: ")
    gateway = input("Enter default gateway: ")
    mask = input("Enter subnet mask or CIDR prefix: ")

    result = diagnose_network(ip, gateway, mask)

    display_report(result)


if __name__ == "__main__":
    main()
