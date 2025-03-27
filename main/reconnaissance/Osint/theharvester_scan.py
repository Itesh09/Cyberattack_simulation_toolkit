# theharvester_scan.py
import subprocess

def run_theharvester(domain):
    """Run theHarvester tool to gather OSINT information."""
    print(f"\n[+] Running theHarvester on {domain}...\n")

    try:
        result = subprocess.run(
            ["theHarvester", "-d", domain, "-l", "500", "-b", "all"],
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except FileNotFoundError:
        print("[-] theHarvester not found. Install it using: sudo apt install theharvester")
