# Program to find the sum of digits of a three-digit number

# Input a three-digit number from the user

num = int(input("Enter a three-digit number: "))

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

sum_of_digits = hundreds + tens + ones

print("\nSum of the digits =", sum_of_digits)
