# brute_force.py
import itertools
import string

def brute_force_crack(target_password, max_length=4):
    """Brute Force Cracking with character combinations."""
    charset = string.ascii_lowercase + string.digits  # Modify as needed
    
    print("[+] Starting Brute Force Attack...")
    
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess_password = ''.join(guess)
            print(f"[*] Trying: {guess_password}")
            
            if guess_password == target_password:
                print(f"[+] Password found: {guess_password}")
                return guess_password
                
    print("[-] Password not found within given constraints.")
    return None
