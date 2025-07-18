import os
from datetime import datetime

# Message to show
message = "Script is running"
print(message)

# Log what happened
log_message = f"{message} at {datetime.now()}"
with open("run_log.txt", "a") as log_file:
    log_file.write(log_message + "\n")

# Check for 'data' folder
data_folder = "data"
if not os.path.exists(data_folder):
    os.makedirs(data_folder)
    print(f"Created missing folder: {data_folder}")
    with open("run_log.txt", "a") as log_file:
        log_file.write(f"Created folder '{data_folder}' at {datetime.now()}\n")

# Create a test file inside data folder
test_file = os.path.join(data_folder, "test.txt")
with open(test_file, "a") as file:
    file.write(f"Ran on {datetime.now()}\n")