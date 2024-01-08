import socket
import argparse

def port_scan(target, ports):
    try:
        # Get IP address if target is a URL
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid URL or unable to resolve the hostname.")
        return

    print(f"Scanning target: {target} ({target_ip})")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Adjust timeout as needed
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()

def main():
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("target", help="URL or IP address to scan")
    parser.add_argument("-p", "--ports", nargs="*", type=int, help="Specific ports to scan")
    parser.add_argument("-n", "--num-ports", type=int, help="Number of ports to scan (first n ports)")

    args = parser.parse_args()

    if args.ports:
        ports_to_scan = args.ports
    elif args.num_ports:
        ports_to_scan = list(range(1, args.num_ports + 1))
    else:
        ports_to_scan = list(range(1, 1001))

    port_scan(args.target, ports_to_scan)

if __name__ == "__main__":
    main()
