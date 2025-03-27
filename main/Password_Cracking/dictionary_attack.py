# dictionary_attack.py
import os
import gzip

DEFAULT_WORDLISTS = [
    "/usr/share/wordlists/rockyou.txt.gz",
    "/usr/share/wordlists/fasttrack.txt",
    "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
]

def dictionary_attack(target_password, wordlist_path=None):
    """Perform a dictionary attack using a predefined or user-specified wordlist."""
    
    if wordlist_path is None:
        print("\n[!] No wordlist provided. Using default wordlists in Kali Linux.")
        for default_list in DEFAULT_WORDLISTS:
            if os.path.exists(default_list):
                wordlist_path = default_list
                print(f"[+] Using: {wordlist_path}")
                break
        else:
            print("[-] No default wordlists found! Install `wordlists` package in Kali.")
            return None

    if not os.path.exists(wordlist_path):
        print(f"[-] Error: Wordlist '{wordlist_path}' not found!")
        return None

    print("[+] Starting Dictionary Attack...")

    # Handle rockyou.txt.gz (compressed)
    if wordlist_path.endswith(".gz"):
        with gzip.open(wordlist_path, 'rt', encoding='utf-8', errors='ignore') as wordlist:
            for word in wordlist:
                word = word.strip()
                print(f"[*] Trying: {word}")
                if word == target_password:
                    print(f"[+] Password found: {word}")
                    return word
    else:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
            for word in wordlist:
                word = word.strip()
                print(f"[*] Trying: {word}")
                if word == target_password:
                    print(f"[+] Password found: {word}")
                    return word

    print("[-] Password not found in wordlist.")
    return None
