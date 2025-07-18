import os
from datetime import datetime, timedelta

days_ago = 5
folder_path = "."
cutoff_time = datetime.now() - timedelta(days=days_ago)

for i, filename in enumerate(os.listdir(folder_path)):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))

        if file_modified_time < cutoff_time:
            print(f"{i+1}.Old file found: {filename}")
            #os.remove(file_path)
            #print(f"✅ Deleted: {filename}")