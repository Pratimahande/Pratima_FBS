# Program to print all numbers in a range divisible by a given number

first = int(input("Enter the first number: "))
last = int(input("Enter the last number: "))
divisor = int(input("Enter the number to check divisibility: "))

print(f"Numbers between {first} and {last} divisible by {divisor} are:")

for i in range(first, last + 1):
    if i % divisor == 0:
        print(i, end=" ")