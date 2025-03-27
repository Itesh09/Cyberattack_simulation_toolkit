# nmap_scan.py
import os

def run_nmap_scan(target):
    """Run Nmap scan with user-selected options."""
    print("\n=== Nmap Network Scanner ===")
    print("1. Normal Scan")
    print("2. Stealth Scan (-sS)")
    print("3. Full Scan (-A -T4)")
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
