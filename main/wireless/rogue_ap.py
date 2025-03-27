import subprocess

def create_rogue_ap(interface="wlan0", ssid="FreeWiFi"):
    """Create a rogue access point using hostapd."""
    try:
        print(f"\n[+] Creating rogue AP '{ssid}' on {interface}...")
        # Step 1: Set up NAT
        subprocess.run(["iptables", "-t", "nat", "-A", "POSTROUTING", "-o", "eth0", "-j", "MASQUERADE"])
        # Step 2: Start hostapd
        with open("hostapd.conf", "w") as f:
            f.write(f"interface={interface}\nssid={ssid}\ndriver=nl80211\nchannel=6")
        subprocess.Popen(["hostapd", "hostapd.conf"])
        # Step 3: Start DHCP server
        subprocess.Popen(["dnsmasq", "-C", "none", "-d", "-i", interface, "--dhcp-range=192.168.1.100,192.168.1.200"])
        print("[!] Rogue AP running. Press Ctrl+C to stop.")
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[!] Stopping rogue AP...")
        subprocess.run(["pkill", "hostapd"])
        subprocess.run(["pkill", "dnsmasq"])
    except Exception as e:
        print(f"[-] Error: {e}")

def rogue_ap_menu():
    """Rogue AP submenu."""
    while True:
        print("\n=== Rogue Access Point ===")
        print("1) Create Rogue AP (hostapd)")
        print("2) Back to Wireless Menu")
        choice = input("Select an option: ")

        if choice == "1":
            interface = input("Enter interface (default: wlan0): ") or "wlan0"
            ssid = input("Enter SSID (default: FreeWiFi): ") or "FreeWiFi"
            create_rogue_ap(interface, ssid)
        elif choice == "2":
            break
        else:
            print("[-] Invalid option.")