from .mitm import mitm_menu
from .dos import dos_menu

def network_attacks_menu():
    """Main network attacks menu."""
    while True:
        print("\n=== Network Attacks ===")
        print("1) Man-in-the-Middle (MITM)")
        print("2) DoS/DDoS Attacks")
        print("3) Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            mitm_menu()
        elif choice == "2":
            dos_menu()
        elif choice == "3":
            break
        else:
            print("[-] Invalid option.")