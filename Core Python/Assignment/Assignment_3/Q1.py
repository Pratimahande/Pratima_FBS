# Program to check if the given number is positive, negative, or zero

# Accept number from user

num = int(input("Enter a number: "))

if num > 0:
    print("The number is +ve.")
elif num < 0:
    print("The number is -ve.")
else:
    print("The number is Zero.")
