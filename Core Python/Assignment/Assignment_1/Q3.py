# Program to find quotient and remainder of two numbers

# Input dividend and divisor from user

dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

quotient = dividend // divisor
remainder = dividend % divisor

print("\nQuotient =", quotient)
print("Remainder =", remainder)
