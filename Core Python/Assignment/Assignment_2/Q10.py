# Program to reverse a three-digit number

# Input a three-digit number from the user

num = int(input("Enter a three-digit number: "))

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

reverse_num = (ones * 100) + (tens * 10) + hundreds

print("\nReversed number =", reverse_num)
