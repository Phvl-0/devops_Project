import os
from datetime import datetime

# Set up file path
data_folder = "data"
log_file = os.path.join(data_folder, "run_log.txt")

# Check if data folder exists
if not os.path.exists(data_folder):
    os.makedirs(data_folder)
    print(f"Created missing folder: {data_folder}")

# Now check if run_log.txt exists
if os.path.exists(log_file):
    # File exists → append message
    with open(log_file, "a") as f:
        f.write(f" Damn Script ran at {datetime.now()}\n")
    print("Log updated")
else:
    # File doesn’t exist → create with header
    with open(log_file, "w") as f:
        f.write(f"# Log created on {datetime.now()}\n")
    print("New log file created")