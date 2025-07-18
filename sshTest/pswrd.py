from datetime import datetime
password = "Anal"
attempts = 0
max_attempts = 3
log = "Login_attempts.log"

print("Login System...\n")
while attempts < max_attempts:
    print("Enter Password below")
    guess = input(':').strip()
    if guess == password:
        print('Access granted!')
        with open(log,"a") as lg:
            lg.write(f"[{datetime.now().strftime('%H:%M:%S')}]- Access granted.\n")
        break
        
    else:
        attempts += 1
        print(f"Wrong!! Attempts left:{max_attempts - attempts}")
        with open(log,"a") as lg:
            lg.write(f"[{datetime.now().strftime('%H:%M:%S')}]- Failed attempt. Remaining:{max_attempts - attempts}\n")
else:
    print('Account Locked!')
    with open(log, "a") as lg:
        lg.write(f"[{datetime.now().strftime('%H:%M:%S')}]- Account Locked due to too many failed attempts.\n")    
print("Exiting login system...")