from datetime import datetime
import os

folder = "logs"
file_name = "app.log"
path = os.path.join(folder, file_name)

if os.path.exists(path):
    print(f"{file_name} already exists in {folder}")
else:
    with open(path, "w") as f:
        f.write("# App Log - Created Automatically\n")
    print(f"{file_name} created in {folder}")

main_log = "run-log.txt"

with open(main_log, "a") as log_file:
    if os.path.exists(path):
        log_file.write(f"Checke{file_name} -> already exists at {datetime.now()}\n")
    else:
        log_file.write(f"Created {file_name} in {folder} at {datetime.now()}\n")
