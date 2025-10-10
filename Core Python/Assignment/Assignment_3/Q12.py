# Program to check if a 3-digit number is a palindrome or not

# Input a 3-digit number

num = int(input("Enter a 3-digit number: "))

original = num

rev = 0
while num > 0:
    digit = num % 10
    rev = (rev * 10) + digit
    num = num // 10

if original == rev:
    print(f"{original} is a Palindrome number.")
else:
    print(f"{original} is not a Palindrome number.")
