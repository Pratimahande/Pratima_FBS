#1) Program to find sum of 1 + 2 + 3 + ... + n

def sum_of_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter the value of n: "))

result = sum_of_natural(n)
print("Sum of series 1 + 2 + 3 + ... +", n, "=", result)


#2) Program to find sum of series 1! + 2! + 3! + ... + n!

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_of_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

n = int(input("Enter the value of n: "))

result = sum_of_factorials(n)
print("Sum of series 1! + 2! + 3! + ... +", n, "! =", result)


# 3)Program to find sum of 1^1 + 2^2 + 3^3 + ... + n^n

def sum_of_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input("Enter the value of n: "))
result = sum_of_powers(n)
print("Sum of series 1^1 + 2^2 + 3^3 + ... +", n, "^", n, "=", result)

