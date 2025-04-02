# masscan_scan.py
import subprocess
from networkscanner.utils import run_tool

def masscan_scan(target):
    """Run Masscan scan."""
    ports = input("Enter ports to scan (default: 1-1000): ") or "1-1000"
    rate = input("Enter scan rate (packets per second, default: 1000): ") or "1000"
    run_tool("masscan", [target, "-p", ports, "--rate", rate])
