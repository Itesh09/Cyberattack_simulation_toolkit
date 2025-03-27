from .wifi_cracking import wifi_cracking_menu
from .rogue_ap import rogue_ap_menu
from .bluetooth import bluetooth_menu

def wireless_menu():
    """Main wireless attack menu."""
    while True:
        print("\n=== Wireless Attacks ===")
        print("1) WiFi Cracking")
        print("2) Rogue Access Point")
        print("3) Bluetooth Attacks")
        print("4) Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            wifi_cracking_menu()
        elif choice == "2":
            rogue_ap_menu()
        elif choice == "3":
            bluetooth_menu()
        elif choice == "4":
            break
        else:
            print("[-] Invalid option.")