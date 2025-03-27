# netdiscover_scan.py
from networkscanner.utils import run_tool

def netdiscover_scan(ip_range):
    """Run Netdiscover scan."""
    run_tool("netdiscover", ["-r", ip_range])
