# Program to calculate Simple Interest

P = int(input("Enter the Principal amount: "))
T = int(input("Enter the Time (in years): "))
R = int(input("Enter the Rate of Interest: "))

SI = (P * T * R) / 100

print("Simple Interest =", SI)
