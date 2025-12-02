# Program to find factorial using recursive function.

def factorial(n):
    if n == 0 or n == 1:     # Base condition
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter number: "))
print("Factorial =", factorial(num))
   