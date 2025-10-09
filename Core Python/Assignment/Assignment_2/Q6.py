# Program to calculate total salary of an employee

# Input basic salary from the user

basic = float(input("Enter the basic salary: "))

da = 0.10 * basic   
ta = 0.12 * basic   
hra = 0.15 * basic  

total_salary = basic + da + ta + hra

print("\nBreakup of salary:")
print("Basic Salary =", basic)
print("Dearness Allowance (DA) =", da)
print("Travel Allowance (TA) =", ta)
print("House Rent Allowance (HRA) =", hra)
print("Total Salary =", total_salary)
