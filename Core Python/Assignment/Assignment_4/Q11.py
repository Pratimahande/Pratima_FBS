# Program to check if a number is a Strong Number

num = int(input("Enter a number: "))
original_num = num

sum = 0
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

while num > 0:
    digit = num % 10
    sum += factorial(digit)
    num //= 10

# Check if it's a strong number

if sum == original_num:
    print(original_num, "is a Strong Number.")
else:
    print(original_num, "is not a Strong Number.")