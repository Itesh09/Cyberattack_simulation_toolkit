# rustscan_scan.py
from NetworkScanner.utils import run_tool

def rustscan_scan(target):
    """Run RustScan scan."""
    ports = input("Enter ports to scan (default: 1-1000): ") or "1-1000"
    run_tool("rustscan", ["-a", target, "-p", ports])
