# Program to check marriage eligibility

# Input gender and age

gender = input("Enter gender (male/female): ").lower()
age = int(input("Enter age: "))

if gender == "male":
    if age >= 21:
        print("You are eligible for marriage.")
    else:
        print("You are not eligible for marriage.")
elif gender == "female":
    if age >= 18:
        print("You are eligible for marriage.")
    else:
        print("You are not eligible for marriage.")
else:
    print("Invalid gender entered. Please enter 'male' or 'female'.")
