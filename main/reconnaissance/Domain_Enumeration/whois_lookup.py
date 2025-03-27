# whois_lookup.py
import whois

def run_whois(domain):
    """Fetch WHOIS information for a domain."""
    print(f"\n[+] Running WHOIS lookup on {domain}...\n")
    try:
        domain_info = whois.whois(domain)
        print(domain_info)
    except Exception as e:
        print(f"[-] Error fetching WHOIS data: {e}")
