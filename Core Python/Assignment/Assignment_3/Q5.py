# Program to check whether a triangle is Equilateral, Isosceles or Scalene

# Input sides of the triangle

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))


if (a + b > c) and (a + c > b) and (b + c > a):   
    if a == b == c:
        print("This is an Equilateral Triangle.")
    elif a == b or b == c or a == c:
        print("This is an Isosceles Triangle.")
    else:
        print("This is a Scalene Triangle.")
else:
    print("The given sides do not form a valid triangle.")

