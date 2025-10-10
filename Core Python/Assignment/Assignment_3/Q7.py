# Program to check if user has entered correct User ID and Password

# Predefined User ID and Password

userid = "admin"
password = "123"

user_input = input("Enter User ID: ")
pass_input = input("Enter Password: ")

if user_input == userid and pass_input == password:
    print(" Login Successful! Welcome.")
else:
    print(" Invalid User ID or Password!")
