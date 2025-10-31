#Program to print all odd numbers until n

n = int(input("Enter the value of n: "))
print(f"Odd numbers from 1 to {n} are:")

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)