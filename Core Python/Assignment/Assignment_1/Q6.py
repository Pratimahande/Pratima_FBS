# Program to find the third angle of a triangle

# Input two angles from the user

angle1 = int(input("Enter first angle of the triangle: "))
angle2 = int(input("Enter second angle of the triangle: "))

angle3 = 180 - (angle1 + angle2)

print("\nThird angle of the triangle =", angle3)
