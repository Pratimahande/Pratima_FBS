# Program to find the roots of a Quadratic Equation

# Equation format: ax² + bx + c = 0

# Input coefficients from the user

import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

D = (b ** 2) - (4 * a * c)


if D > 0:

    root1 = (-b + math.sqrt(D)) / (2 * a)
    root2 = (-b - math.sqrt(D)) / (2 * a)
    print("\nRoots are real and distinct:")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif D == 0:
    
    root = -b / (2 * a)
    print("\nRoots are real and equal:")
    print("Root 1 = Root 2 =", root)

else:

    realPart = -b / (2 * a)
    imagPart = math.sqrt(-D) / (2 * a)
    print("\nRoots are complex and imaginary:")
    print("Root 1 = {:.2f} + {:.2f}i".format(realPart, imagPart))
    print("Root 2 = {:.2f} - {:.2f}i".format(realPart, imagPart))
