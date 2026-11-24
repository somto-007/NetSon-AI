
import ipaddress


def validate_ip(ip_address):
    if not isinstance(ip_address, str):
        return None

    try:
        return ipaddress.IPv4Address(ip_address.strip())
    except ipaddress.AddressValueError:
        return None


def is_usable_host(address, network):
    if network.prefixlen >= 31:
        return True

    return address not in (
        network.network_address,
        network.broadcast_address
    )


def create_result(status, problem, recommendation):
    return {
        "status": status,
        "problem": problem,
        "recommendation": recommendation
    }


def diagnose_network(ip_address, gateway, subnet_mask):

    ip = validate_ip(ip_address)
    gw = validate_ip(gateway)

    if ip is None:
        return create_result(
            "error",
            "Invalid device IP address.",
            "Enter a valid IPv4 address for the device."
        )

    if gw is None:
        return create_result(
            "error",
            "Invalid gateway address.",
            "Enter a valid IPv4 address for the gateway."
        )

    if ip == gw:
        return create_result(
            "error",
            "Device IP and gateway addresses are identical.",
            "Configure a separate valid gateway address."
        )

    if not isinstance(subnet_mask, str):
        return create_result(
            "error",
            "Invalid subnet mask.",
            "Enter a valid IPv4 subnet mask or CIDR prefix."
        )

    mask = subnet_mask.strip()

    if mask.startswith("/"):
        mask = mask[1:]

    try:
        network = ipaddress.IPv4Network(
            f"{ip}/{mask}",
            strict=False
        )
    except (ipaddress.AddressValueError,
            ipaddress.NetmaskValueError):
        return create_result(
            "error",
            "Invalid subnet mask.",
            "Enter a valid IPv4 subnet mask or CIDR prefix."
        )

    if not is_usable_host(ip, network):
        return create_result(
            "error",
            "Device IP is a reserved network or broadcast address.",
            "Assign a usable host address to the device."
        )

    if gw not in network:
        return create_result(
            "warning",
            "Gateway is outside the device subnet.",
            "Check the IP, subnet and routing configuration."
        )

    if not is_usable_host(gw, network):
        return create_result(
            "error",
            "Gateway is a reserved network or broadcast address.",
            "Configure a usable host address as the gateway."
        )

    return create_result(
        "success",
        "No subnet configuration issue detected.",
        "Next, test connectivity to the gateway."
    )
