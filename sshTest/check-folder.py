from datetime import datetime
import os

folder = "logs"
if os.path.exists(folder):
    print(f"{folder} already exists!")
    with open("folder-log.txt","a") as log:
        log.write(f"The folder '{folder}'-> already exists at {datetime.now()}\n ")
else:
    os.makedirs(folder)
    print(f"'{folder}' folder created!")
    with open("folder-log.txt","a") as log:
        log.write(f"Created folder '{folder}' at {datetime.now()}\n")	