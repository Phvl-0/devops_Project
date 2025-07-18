valid = False

while not valid:
    user_input = print("Enter a number btn 1-10")
    user_input = input(":")
    if user_input.isdigit() and 1<= int(user_input) <=10:
        valid = True
    else:
        print("Invalid! Try again.")
print(f"You entered:'{user_input}'")