import os
import subprocess

from reconnaissance.Domain_Enumeration.dns_enum import run_dnsenum
from reconnaissance.Domain_Enumeration.sublist_enum import run_sublist3r
from reconnaissance.Domain_Enumeration.whois_lookup import run_whois
from reconnaissance.Osint.theharvester_scan import run_theharvester
from reconnaissance.Osint.shodan_scan import run_shodan_scan
from reconnaissance.Osint.google_dorking import google_dork
from reconnaissance.networkscanner.nmap_Scan import run_nmap_scan
from reconnaissance.networkscanner.masscan_scan import masscan_scan
from reconnaissance.networkscanner.rustscan import rustscan_scan
from reconnaissance.networkscanner.amass_scan import amass_scan
from reconnaissance.networkscanner.netdiscover_scan import netdiscover_scan
from Password_Cracking.brute_force import brute_force_crack
from Password_Cracking.dictionary_attack import dictionary_attack
from Password_Cracking.utils import get_target_password
import Web_Apps.xss as xss
import Web_Apps.sql as sqli
import Web_Apps.csrf as csrf
import Web_Apps.file_inclusion as lfi
from Exploitation.vulnerability_scanner import nmap_vuln_scan
from Exploitation.vulnerability_scanner import searchsploit_exploits
from Exploitation.vulnerability_scanner import nikto_scan
from Exploitation.vulnerability_scanner import wpscan_scan
from Exploitation.network_exploits import *
from Exploitation.reverse_shells import *
from Exploitation.vulnerability_scanner import *
from Network_Attack_Tools import network_attacks_menu
from wireless import wireless_menu
from Social_enginering_Simulation import social_engineering_menu




# Banner
BANNER = """
███████╗███████╗████████╗██╗   ██╗██╗   ██╗ ██████╗ ██████╗ 
██╔════╝██╔════╝╚══██╔══╝██║   ██║██║   ██║██╔═══██╗██╔══██╗
█████╗  █████╗     ██║   ██║   ██║██║   ██║██║   ██║██║  ██║
██╔══╝  ██╔══╝     ██║   ██║   ██║██║   ██║██║   ██║██║  ██║
███████╗███████╗   ██║   ╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝
╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ 
                 eEtuu_09 Version 1.2 
"""

# Main Menu Options
MAIN_MENU = """
1) Disclaimer and Manual
2) Reconnaissance
3) Exploitation
4) Password Cracking
5) Social Engineering Simulation
6) Network Attack Tools
7) Wireless Attack Tools
8) Web Application Tools
9) Mobile and IoT Attack Tools
10) Reporting
11) Exit
"""

# Reconnaissance Submenu
RECON_MENU = """
1) Network Scan
2) OSINT (Open Source Intelligence)
3) Domain Enumeration
4) Back to Main Menu
"""

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    """Display the banner."""
    clear_screen()
    print(BANNER)

def disclaimer():
    """Display disclaimer and manual."""
    display_banner()
    print("""
DISCLAIMER:
This toolkit is intended for educational and authorized penetration testing purposes only.
Unauthorized use of this toolkit for malicious purposes is strictly prohibited.
The developers are not responsible for any misuse of this software.

MANUAL:
1) Select an option from the main menu.
2) Follow the prompts to use the tools.
3) Always ensure you have proper authorization before running any scans or attacks.
""")
    input("\nPress Enter to return to the main menu...")

def reconnaissance():
    """Reconnaissance module."""
    while True:
        display_banner()
        print(RECON_MENU)
        choice = input("Select an option: ")

        if choice == "1":
            network_scan_menu()
        elif choice == "2":
            osint()
        elif choice == "3":
            domain_enumeration()
        elif choice == "4":
            break
        else:
            print("\n[-] Invalid option. Please try again.")
            input("\nPress Enter to continue...")


# OSINT Submenu
OSINT_MENU = """
1) Shodan Scan
2) theHarvester
3) Google Dorking
4) Back to Reconnaissance Menu
"""

def osint():
    """OSINT Menu"""
    while True:
        os.system("clear")
        print("\n🔍 OSINT (Open Source Intelligence) 🔍")
        print(OSINT_MENU)
        choice = input("Select an option: ")

        if choice == "1":
            target = input("Enter target IP/Domain for Shodan: ")
            run_shodan_scan(target)
        elif choice == "2":
            domain = input("Enter domain for theHarvester: ")
            run_theharvester(domain)
        elif choice == "3":
            query = input("Enter Google Dork query: ")
            google_dork(query)
        elif choice == "4":
            break
        else:
            print("\n[-] Invalid option. Please try again.")
        input("\nPress Enter to continue...")


# Domain Enumeration Submenu
DOMAIN_ENUM_MENU = """
1) DNS Enumeration (dnsenum)
2) Subdomain Enumeration (Sublist3r)
3) WHOIS Lookup
4) Back to Reconnaissance Menu
"""

def domain_enumeration():
    """Domain Enumeration Menu."""
    while True:
        os.system("clear")
        print("\n🔍 Domain Enumeration 🔍")
        print(DOMAIN_ENUM_MENU)
        choice = input("Select an option: ")

        if choice == "1":
            domain = input("Enter domain for DNS Enumeration: ")
            run_dnsenum(domain)
        elif choice == "2":
            domain = input("Enter domain for Subdomain Enumeration: ")
            run_sublist3r(domain)
        elif choice == "3":
            domain = input("Enter domain for WHOIS Lookup: ")
            run_whois(domain)
        elif choice == "4":
            break
        else:
            print("\n[-] Invalid option. Please try again.")
        input("\nPress Enter to continue...")

def network_scan_menu():
    """Network Scan submenu with tool descriptions."""
    while True:
        os.system("clear")
        print("\n=== Network Scan ===")
        print("1) Nmap ------------------- Use it for detailed network scanning, service detection, and OS fingerprinting.")
        print("2) Masscan ---------------- Use it for extremely fast port scanning of large networks.")
        print("3) RustScan --------------- Use it for fast port scanning with Rust-based performance.")
        print("4) Amass ------------------ Use it for subdomain enumeration and DNS mapping.")
        print("5) Netdiscover ------------ Use it for ARP-based discovery of live hosts on a local network.")
        print("6) Back to Reconnaissance Menu")
        
        choice = input("Select an option: ")

        if choice == "1":
            target = input("Enter target IP or hostname: ")
            run_nmap_scan(target)
        elif choice == "2":
            target = input("Enter target IP or range: ")
            masscan_scan(target)
        elif choice == "3":
            target = input("Enter target IP or hostname: ")
            rustscan_scan(target)
        elif choice == "4":
            domain = input("Enter domain to enumerate: ")
            amass_scan(domain)
        elif choice == "5":
            ip_range = input("Enter IP range (e.g., 192.168.1.0/24): ")
            netdiscover_scan(ip_range)
        elif choice == "6":
            break
        else:
            print("[-] Invalid option. Please try again.")
        
        input("\nPress Enter to continue...")

def password_cracking_menu():
    """Password Cracking submenu."""
    while True:
        os.system("clear")
        print("\n=== Password Cracking ===")
        print("1) Brute Force Cracking ---- Try all possible combinations")
        print("2) Dictionary Attack ------- Use a predefined wordlist")
        print("3) Back to Main Menu")
        
        choice = input("Select an option: ")

        if choice == "1":
            password = get_target_password()
            max_length = int(input("Enter max password length for brute force (default: 4): ") or "4")
            brute_force_crack(password, max_length)
        elif choice == "2":
            password = get_target_password()
            wordlist_path = input("Enter path to wordlist file: ")
            dictionary_attack(password, wordlist_path)
        elif choice == "3":
            break
        else:
            print("[-] Invalid option. Please try again.")

        input("\nPress Enter to continue...")


def banner():
    """Display banner."""
    print("\n" + "="*40)
    print("  Cyberattack Simulation Toolkit  ")
    print("="*40)
    print("Developed for Web Application Testing\n")

def web_attack_menu():
    """Main menu for Web Application Attacks."""
    while True:
        os.system("clear" if os.name == "posix" else "cls")  # Clear screen
        banner()
        print("1) XSS (Cross-Site Scripting)")
        print("2) SQL Injection")
        print("3) CSRF (Cross-Site Request Forgery)")
        print("4) Local File Inclusion (LFI)")
        print("5) Exit")
        
        choice = input("\nSelect an attack module (1-5): ")
        
        if choice == "1":
            xss.xss_attack()
        elif choice == "2":
            sqli.sqli_attack()
        elif choice == "3":
            csrf.csrf_attack()
        elif choice == "4":
            lfi.lfi_attack()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("[-] Invalid choice, please try again.")

        input("\nPress Enter to continue...") 


def vulnerability_scanner_menu():
    """Vulnerability Scanner submenu."""
    while True:
        print("\n=== Vulnerability Scanner ===")
        print("1) Nmap Vulnerability Scan (NSE)")
        print("2) Searchsploit (Find Exploits)")
        print("3) Nikto (Web Server Scanner)")
        print("4) WPScan (WordPress Scanner)")
        print("5) Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            target = input("Enter target IP/hostname: ")
            nmap_vuln_scan(target)
        elif choice == "2":
            query = input("Enter search query (e.g., 'Apache 2.4.49'): ")
            searchsploit_exploits(query)
        elif choice == "3":
            target = input("Enter target URL (e.g., http://example.com): ")
            nikto_scan(target)
        elif choice == "4":
            target = input("Enter WordPress site URL (e.g., http://example.com): ")
            wpscan_scan(target)
        elif choice == "5":
            break
        else:
            print("[-] Invalid option. Try again.")
        sleep(1)  # Pause for readability

def network_exploits_menu():
    """Network Exploits submenu."""
    while True:
        print("\n=== Network Exploits ===")
        print("1) Exploit SMB (e.g., EternalBlue)")
        print("2) SSH Bruteforce")
        print("3) Exploit RDP (e.g., BlueKeep)")
        print("4) Metasploit (Custom Exploit)")
        print("5) Reverse shell")
        print("6)  Common vulnerabilities")
        print("7) Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            target = input("Enter target IP: ")
            exploit_smb(target)
        elif choice == "2":
            target = input("Enter target IP: ")
            username = input("Enter username: ")
            wordlist = input("Enter wordlist path: ")
            ssh_bruteforce(target, username, wordlist)
        elif choice == "3":
            target = input("Enter target IP: ")
            exploit_rdp(target)
        elif choice == "4":
            target = input("Enter target IP: ")
            exploit_path = input("Enter Metasploit exploit path (e.g., exploit/windows/smb/...): ")
            metasploit_exploit(target, exploit_path)
        elif choice == "5":
            reverse_shells_menu()
        
        elif choice == "6":
            vulnerability_scanner_menu()

        elif choice == "7":
            break
        else:

            print("[-] Invalid option. Try again.")
        sleep(1)  # Pause for readability
def main_menu():
    """Main menu for the toolkit."""
    while True:
        display_banner()
        print(MAIN_MENU)
        choice = input("Select an option: ")

        if choice == "1":
            disclaimer()
        elif choice == "2":
            reconnaissance()
        elif choice == "3":
           vulnerability_scanner_menu()
        elif choice == "4":
            password_cracking_menu()
            
        elif choice == "5":
            social_engineering_menu()
        elif choice == "6":
            network_attacks_menu()
           
        elif choice == "7":
            wireless_menu()
        elif choice == "8":
            web_attack_menu()
        elif choice == "9":
            print("\n[+] Mobile and IoT Attack Tools module is under development.")
            input("\nPress Enter to continue...")
        elif choice == "10":
            print("\n[+] Reporting module is under development.")
            input("\nPress Enter to continue...")
        elif choice == "11":
            print("\n[+] Exiting the toolkit. Goodbye!")
            break
        else:
            print("\n[-] Invalid option. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
