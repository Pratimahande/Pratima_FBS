# Program to calculate Compound Interest

# Input values from the user

P = int(input("Enter the Principal amount (P): "))
T = int(input("Enter the Time in years (T): "))
R = int(input("Enter the Rate of Interest (R): "))

A = P * (1 + R / 100) ** T   
CI = A - P                   

print("\nCompound Interest = {:.2f}".format(CI))
print("Total Amount = {:.2f}".format(A))
