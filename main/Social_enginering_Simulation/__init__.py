from .phishing import phishing_menu
from .credential_harvesting import credential_menu
from .usb_drop import usb_menu

def social_engineering_menu():
    """Main social engineering menu."""
    while True:
        print("\n=== Social Engineering ===")
        print("1) Phishing Kits")
        print("2) Credential Harvesting")
        print("3) USB Drop Attacks")
        print("4) Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            phishing_menu()
        elif choice == "2":
            credential_menu()
        elif choice == "3":
            usb_menu()
        elif choice == "4":
            break
        else:
            print("[-] Invalid option.")