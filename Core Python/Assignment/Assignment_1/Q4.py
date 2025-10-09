# Program to calculate Simple Interest

# Input values from the user

P = int(input("Enter the Principal amount (P): "))
T = int(input("Enter the Time in years (T): "))
R = int(input("Enter the Rate of Interest (R): "))

SI = (P * T * R) / 100


print("\nSimple Interest = {:.2f}".format(SI))
