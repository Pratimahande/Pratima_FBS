# Program to swap two numbers without using a third variable

# Input two numbers from the user

x = int(input("Enter first number (x): "))
y = int(input("Enter second number (y): "))

print("\nBefore swapping:")
print("x =", x)
print("y =", y)

x = x + y
y = x - y
x = x - y

print("\nAfter swapping:")
print("x =", x)
print("y =", y)
