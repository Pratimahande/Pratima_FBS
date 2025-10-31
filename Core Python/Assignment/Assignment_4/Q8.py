# Program to find numbers divisible by 7 and multiples of 5 in a given range

first = int(input("Enter the first number: "))
last = int(input("Enter the last number: "))

print(f"Numbers between {first} and {last} that are divisible by 7 and multiples of 5:")

for i in range(first, last + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")