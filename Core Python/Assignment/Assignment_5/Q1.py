# Program to prompt user for User ID and Password using a loop (3 attempts)

id = "admin"
password = "123"

for attempt in range(1, 4):
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")

    if user_id == id and password == password:
        print("Login successful")
        break
    else:
        # If incorrect and not the last attempt
        if attempt < 3:
            print(f"Incorrect credentials. Try again ({3 - attempt} attempt(s) left).\n")
        else:
            print("Too many failed attempts. Access end.")