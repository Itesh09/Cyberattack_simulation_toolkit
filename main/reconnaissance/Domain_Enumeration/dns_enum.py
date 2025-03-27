# dns_enum.py
import subprocess

def run_dnsenum(domain):
    """Runs dnsenum to enumerate DNS records."""
    print(f"\n[+] Running dnsenum on {domain}...\n")
    try:
        result = subprocess.run(["dnsenum", domain], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("[-] dnsenum not found. Please install it using: sudo apt install dnsenum")
