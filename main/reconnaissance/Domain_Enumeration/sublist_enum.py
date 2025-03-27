# sublist_enum.py
import subprocess

def run_sublist3r(domain):
    """Runs Sublist3r to enumerate subdomains."""
    print(f"\n[+] Running Sublist3r on {domain}...\n")
    try:
        result = subprocess.run(["sublist3r", "-d", domain], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("[-] Sublist3r not found. Install it using: pip install sublist3r")
