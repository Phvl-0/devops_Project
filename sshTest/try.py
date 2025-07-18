"""
def file_checker(file):
    try:
        with open(file,"r") as f:
            read_file = f.read()
            print(read_file)

    except FileNotFoundError:
        print(f"'{file}' file does not exist!...Please create it.")
    except PermissionError:
        print(f"Access Denied!...Permission requied to read '{file}'.")
    except Exception as e:
        print(f"{type(e).__name__}: {e} ")
  
file_checker("system-run-log.txt")
"""

# try.py (or test_permission_error.py)

def file_checker(file_path):
    try:
        with open(file_path, "r") as f:
            read_content = f.read()
            print(f"Successfully read content from '{file_path}':")
            print(read_content)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist! Please create it.")
    except PermissionError:
        print(f"Access Denied! Permission required to read '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred ({type(e).__name__}): {e}")

# --- Call the function to test the permissions ---
# Make sure this matches the file you did chmod on!
file_checker("system-run-log.txt")

print("\nScript finished trying to access the file.")