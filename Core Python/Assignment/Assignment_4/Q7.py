# Program to print all integers up to n that aren't divisible by 2 and 3

n = int(input("Enter a number: "))

print("Numbers not divisible by 2 and 3 up to", n, "are:")

for i in range(1, n + 1):
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=" ") 