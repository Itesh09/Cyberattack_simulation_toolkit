# google_dorking.py
import webbrowser

def google_dork(query):
    """Perform Google Dorking based on the user's query."""
    print("\n[+] Opening Google search with dorking query...\n")
    
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    print(f"[+] Searching: {search_url}")
