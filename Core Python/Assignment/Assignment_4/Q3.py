# Program to print sum of series up to n

n = int(input("Enter the value of n: "))

sum_series = 0

for i in range(1, n + 1):
    sum_series += i

print(f"The sum of series up to {n} is:{sum_series}")