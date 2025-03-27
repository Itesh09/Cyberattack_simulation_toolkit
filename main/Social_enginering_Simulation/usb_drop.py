import os

def generate_payload(payload_type):
    """Generate malicious USB payload."""
    payloads = {
        "1": "windows_reverse_shell.ps1",
        "2": "linux_backdoor.sh",
        "3": "rubber_ducky_script.txt"
    }
    if payload_type in payloads:
        print(f"\n[+] Generated {payloads[payload_type]} in /payloads/")
        # In a real tool, you'd generate actual payload files
    else:
        print("[-] Invalid payload type.")

def usb_menu():
    """USB drop attack menu."""
    while True:
        print("\n=== USB Drop Attacks ===")
        print("1) Windows Reverse Shell")
        print("2) Linux Backdoor")
        print("3) Rubber Ducky Script")
        print("4) Back to Social Engineering")
        choice = input("Select an option: ")

        if choice in ["1", "2", "3"]:
            generate_payload(choice)
        elif choice == "4":
            break
        else:
            print("[-] Invalid option.")