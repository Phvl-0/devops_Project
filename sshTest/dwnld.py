import os  
for file in os.listdir("."):  
    size = os.path.getsize(file)  # New concept: filesize  
    if size > 100_000_000:  # 100MB  
        print(f"⚠️ {file} is {size} bytes!")  