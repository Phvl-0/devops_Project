from datetime import datetime

message = "Script is running"
print(message)

with open("run_log.txt", "a") as log_file:
    log_file.write(f"{message} at {datetime.now()}\n")