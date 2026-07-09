import socket
import time

# ==========================================
#           TCP PORT SCANNER
# ==========================================

print("=" * 40)
print("        TCP PORT SCANNER")
print("      Made by @de4ault.93")
print("=" * 40)

# Ask the user for the target IP address
target_ip = input("Target IP: ")

# Ask if the user wants to scan common ports
scan_choice = input("Scan famous ports? (y/n): ").lower()


def scan_port(target_ip, port):
    """
    Scans a single TCP port and prints the result.
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target_ip, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")

        try:
            service = socket.getservbyport(port, "tcp")
        except OSError:
            service = "Unknown"

        print(f"    Service: {service}")

    else:
        print(f"[-] Port {port} is closed")

    sock.close()


if scan_choice == "y":

    famous_ports = [
        21, 22, 23, 25,
        53, 80, 110, 111,
        135, 139, 143,
        443, 993, 995
    ]

    start = time.time()

    for port in famous_ports:
        scan_port(target_ip, port)

    end = time.time()

    print(f"\nScan completed in {end - start:.2f} seconds.")

elif scan_choice == "n":

    input_ports = input("Enter ports to scan (comma-separated): ")

    ports = [int(port.strip()) for port in input_ports.split(",")]

    start = time.time()

    for port in ports:
        scan_port(target_ip, port)

    end = time.time()

    print(f"\nScan completed in {end - start:.2f} seconds.")

else:
    print("Invalid option. Please enter 'y' or 'n'.")