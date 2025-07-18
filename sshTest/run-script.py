import subprocess
from datetime import datetime

main_log = "log.txt"

def run_script(script_name):
    print(f"Running {script_name}...")  # No need for `msg` variable
    result = subprocess.run(["python", script_name], capture_output=True, text=True)

    if result.stdout:
        print(f"Output: {result.stdout.strip()}")  # Direct print
    if result.stderr:
        print(f"Error: {result.stderr.strip()}")  # Direct print

    with open(main_log, "a") as log:  # Use the variable
        log.write(f"[{datetime.now()}] Ran {script_name}\n")
        if result.stdout:
            log.write(f"OUTPUT: {result.stdout.strip()}\n")
        if result.stderr:
            log.write(f"ERROR: {result.stderr.strip()}\n")  # Fixed typo

run_script("check-folder.py")
run_script("check-file.py")