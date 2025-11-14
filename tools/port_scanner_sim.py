# Simple Port Scanner Simulation
# This does NOT scan a real network.
# It simulates the logic of checking open ports on a system.

# A fake list of ports and their statuses
fake_ports = {
    22: "open",
    80: "open",
    443: "open",
    21: "closed",
    3389: "closed",
    53: "open"
}

def check_port(port_number):
    """Check if a port is open or closed in the simulated list."""
    if port_number in fake_ports:
        return fake_ports[port_number]
    else:
        return "unknown (not in simulated list)"

print("Port Scanner Simulation")
print("Enter a port number to check its status (or type 'exit' to quit).")

while True:
    user_input = input("> ")

    if user_input.lower() == "exit":
        print("Exiting port scanner. Goodbye!")
        break

    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    port = int(user_input)
    status = check_port(port)

    print(f"Port {port} is: {status.upper()}")
