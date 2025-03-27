# utils.py
import subprocess

def run_tool(tool, args):
    """Run a tool with the provided arguments."""
    try:
        command = [tool] + args
        print(f"[+] Running {tool} with command: {' '.join(command)}")
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print(f"[-] Error: {tool} is not installed or not in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error: {tool} failed with exit code {e.returncode}.")
