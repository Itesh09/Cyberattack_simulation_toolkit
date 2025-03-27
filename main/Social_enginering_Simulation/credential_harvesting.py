import os
import subprocess

def create_fake_page(service):
    """Generate a fake login page."""
    templates = {
        "facebook": "facebook_login.html",
        "google": "google_login.html"
    }
    if service in templates:
        print(f"\n[+] Fake {service} page created: {templates[service]}")
        # In a real tool, you'd copy from a template directory
    else:
        print("[-] Template not available.")

def start_ngrok(port=8080):
    """Expose local server via ngrok."""
    try:
        print("\n[+] Starting ngrok...")
        subprocess.Popen(["ngrok", "http", str(port)])
        print("[!] Check ngrok console for public URL")
    except FileNotFoundError:
        print("[-] Install ngrok: https://ngrok.com/download")

def credential_menu():
    """Credential harvesting menu."""
    while True:
        print("\n=== Credential Harvesting ===")
        print("1) Create Fake Login Page")
        print("2) Expose with Ngrok")
        print("3) Back to Social Engineering")
        choice = input("Select an option: ")

        if choice == "1":
            service = input("Enter service (e.g., facebook/google): ").lower()
            create_fake_page(service)
        elif choice == "2":
            port = input("Enter local port (default: 8080): ") or "8080"
            start_ngrok(int(port))
        elif choice == "3":
            break
        else:
            print("[-] Invalid option.")