import re

def validate_ip(ip_address):
    """Validate an IP address using a regular expression."""
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(pattern, ip_address))

def split_ip_addresses(ip_address):
    """Split an IP address into its octets."""
    octets = []
    for part in ip_address.split('.'):
        octets.append(int(part))
    return octets

if __name__ == "__main__":
    while True:
        ip_address = input("Enter an IP address: ")
        if validate_ip(ip_address):
            break
        else:
            print("Invalid IP address. Please try again.")

    octets = split_ip_addresses(ip_address)
    for i, octet in enumerate(octets):
        print(f"IP {i+1}: {octet}")