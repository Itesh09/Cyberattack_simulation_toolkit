# amass_scan.py
from .utils import run_tool

def amass_scan(domain):
    """Run Amass scan."""
    run_tool("amass", ["enum", "-d", domain])
