# shodan_scan.py
import shodan

SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"  # Replace with your API key

def run_shodan_scan(target):
    """Perform a Shodan search on a given IP or domain."""
    print(f"\n[+] Running Shodan scan on {target}...\n")
    
    try:
        api = shodan.Shodan(SHODAN_API_KEY)
        result = api.search(target)
        
        for host in result['matches']:
            print(f"IP: {host['ip_str']}")
            print(f"Port: {host.get('port', 'N/A')}")
            print(f"Organization: {host.get('org', 'N/A')}")
            print(f"Operating System: {host.get('os', 'N/A')}")
            print("-" * 50)
            
    except shodan.APIError as e:
        print(f"[-] Shodan API error: {e}")

