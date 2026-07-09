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
Target_ip = input("Target IP: ")

# Ask if the user wants to scan common ports
target_ports2 = input("Scan famous ports? (y/n): ")

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

        # Create a new socket for this port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        # Try connecting to the target IP on the current port
        result = sock.connect_ex((Target_ip, port))

        # If result is 0, the port is open
        if result == 0:
            print(f"[+] Port {port} is open.")
        else:
            print(f"[-] Port {port} is unreachable.")

        # Close the socket before moving to the next port
        sock.close()

# If the user wants to choose their own ports
elif target_ports2 == "n":

    # Ask for ports separated by commas
    input_ports = input("Enter ports to scan (comma-separated): ")

    # Convert the input into a list of integers
    ports = [int(port.strip()) for port in input_ports.split(",")]

    # Loop through every chosen port
    for port in ports:

        # Create a new socket for this port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        # Attempt a TCP connection
        result = sock.connect_ex((Target_ip, port))

        # Port is open
        if result == 0:
            print(f"[+] Port {port} is open.")
        else:
            print(f"[-] Port {port} is unreachable.")

        # Close the socket
        sock.close()