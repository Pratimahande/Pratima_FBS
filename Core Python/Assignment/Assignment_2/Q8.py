# Program to swap two numbers using a third variable

# Input two numbers from the user

x = int(input("Enter first number (x): "))
y = int(input("Enter second number (y): "))

print("\nBefore swapping:")
print("x =", x)
print("y =", y)

temp = x
x = y
x = temp

print("\nAfter swapping:")
print("x =", x)
print("x =", y)
