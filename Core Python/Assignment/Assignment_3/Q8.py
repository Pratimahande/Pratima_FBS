# Program to verify user ID and password with captcha system

import random

# Step 1: Predefined user credentials

userid = "admin"
password = "123"

# Step 2: Ask user for login details

user_input = input("Enter User ID: ")
pass_input = input("Enter Password: ")

# Step 3: Verify credentials

if user_input == userid and pass_input == password:
    print("\nLogin successful! Please verify captcha to continue.\n")

    # Step 4: Generate 4-digit random number as captcha

    captcha = random.randint(1000, 9999)
    print(f"Captcha: {captcha}")

    # Step 5: Ask user to re-enter the captcha

    user_captcha = int(input("Enter the above number: "))

    # Step 6: Verify captcha

    if user_captcha == captcha:
        print("\n Login Verified Successfully!")
    else:
        print("\n Verification Failed! Incorrect captcha.")
else:
    print("\n Invalid User ID or Password!")
