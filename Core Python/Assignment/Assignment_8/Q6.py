# Program to print Fibonacci series up to n terms

def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for i in range(n):
        print(b, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of terms: "))
fibonacci_series(n)
