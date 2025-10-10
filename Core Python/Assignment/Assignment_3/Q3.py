# Program to check whether a triangle is valid or not based on its angles

# Input three angles of the triangle

a1 = float(input("Enter first angle: "))
a2 = float(input("Enter second angle: "))
a3 = float(input("Enter third angle: "))

if (a1 + a2 + a3 == 180) and (a1 > 0 and a2 > 0 and a3 > 0):
    print(" The triangle is valid.")
else:
    print(" The triangle is not valid.")
