'''import os
import subprocess

def run_tool(tool, args):
    """Run a tool with the provided arguments."""
    try:
        command = [tool] + args
        print(f"[+] Running {tool} with command: {' '.join(command)}")
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print(f"[-] Error: {tool} is not installed or not in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error: {tool} failed with exit code {e.returncode}.")

def run_nmap_scanner(target):
    """Run Nmap scan with user-selected options."""
    print("\n=== Nmap Network Scanner ===")
    print("1. Normal Scan")
    print("2. Stealth Scan")
    print("3. Full Scan")
    choice = input("Select a scan type (1-3): ")

    if choice == "1":
        os.system(f"nmap {target}")
    elif choice == "2":
        os.system(f"nmap -sS {target}")
    elif choice == "3":
        os.system(f"nmap -A -T4 {target}")
    else:
        print("[-] Invalid choice. Using default Nmap scan.")
        os.system(f"nmap {target}")

def masscan_scan(target):
    """Run Masscan scan."""
    ports = input("Enter ports to scan (default: 1-1000): ") or "1-1000"
    rate = input("Enter scan rate (packets per second, default: 1000): ") or "1000"
    run_tool("masscan", [target, "-p", ports, "--rate", rate])

def rustscan_scan(target):
    """Run RustScan scan."""
    ports = input("Enter ports to scan (default: 1-1000): ") or "1-1000"
    run_tool("rustscan", ["-a", target, "-p", ports])

def amass_scan(domain):
    """Run Amass scan."""
    run_tool("amass", ["enum", "-d", domain])

def netdiscover_scan(range):
    """Run Netdiscover scan."""
    run_tool("netdiscover", ["-r", range])

def network_scan_menu():
    """Network Scan submenu with tool descriptions."""
    while True:
        print("\n=== Network Scan ===")
        print("1) Nmap ------------------- Use it for detailed network scanning, service detection, and OS fingerprinting.")
        print("2) Masscan ---------------- Use it for extremely fast port scanning of large networks.")
        print("3) RustScan --------------- Use it for fast port scanning with Rust-based performance.")
        print("4) Amass ------------------ Use it for subdomain enumeration and DNS mapping.")
        print("5) Netdiscover ------------ Use it for ARP-based discovery of live hosts on a local network.")
        print("6) Back to Reconnaissance Menu")
        choice = input("Select an option: ")

        if choice == "1":
            target = input("Enter target IP or hostname: ")
            run_nmap_scanner(target)
            input("\nPress Enter to continue...")
        elif choice == "2":
            target = input("Enter target IP or range: ")
            masscan_scan(target)
            input("\nPress Enter to continue...")
        elif choice == "3":
            target = input("Enter target IP or hostname: ")
            rustscan_scan(target)
            input("\nPress Enter to continue...")
        elif choice == "4":
            domain = input("Enter domain to enumerate: ")
            amass_scan(domain)
            input("\nPress Enter to continue...")
        elif choice == "5":
            range = input("Enter IP range (e.g., 192.168.1.0/24): ")
            netdiscover_scan(range)
            input("\nPress Enter to continue...")
        elif choice == "6":
            break
        else:
            print("[-] Invalid option. Please try again.")
            input("\nPress Enter to continue...")"
'''