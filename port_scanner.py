import socket
import time

# ==========================================
#           TCP PORT SCANNER
# ==========================================
print("=" * 40)
print("=       TCP PORT SCANNER")
print("=     Made by @de4ault.93")
print("=" * 40)

# Ask the user for the target IP address
Target_ip = input("Target IP: ")

# Ask if the user wants to scan common ports
target_ports2 = input("Scan famous ports? (y/n): ")

# Create a TCP (SOCK_STREAM) IPv4 (AF_INET) socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wait at most 1 second before considering a port unreachable
sock.settimeout(1)

# If the user chose to scan common ports
if target_ports2 == "y":

    # List of the most common TCP ports
    famous_ports = [
        21, 22, 23, 25,
        53, 80, 110, 111,
        135, 139, 143,
        443, 993, 995
    ]

    # Loop through every port in the list
    for port in famous_ports:

        # Try connecting to the target IP on the current port.
        # connect_ex() returns 0 if the connection succeeds.
        result = sock.connect_ex((Target_ip, port))

        # If result is 0, the port is open
        if result == 0:
            print(f"[+] Port {port} is open.")

        # Otherwise the port is closed or unreachable
        else:
            print(f"[-] Port {port} is unreachable.")

# If the user wants to choose their own ports
elif target_ports2 == "n":

    # Ask for ports separated by commas
    input_ports = input("Enter ports to scan (comma-separated): ")

    # Convert the input into a list of integers.
    # Example: "22,80,443" -> [22, 80, 443]
    ports = [int(port.strip()) for port in input_ports.split(",")]

    # Loop through every chosen port
    for port in ports:

        # Attempt a TCP connection
        result = sock.connect_ex((Target_ip, port))

        # Port is open
        if result == 0:
            print(f"[+] Port {port} is open.")

        # Port is closed or unreachable
        else:
            print(f"[-] Port {port} is unreachable.")