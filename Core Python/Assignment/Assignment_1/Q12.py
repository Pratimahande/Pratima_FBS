# Program to find the volume of a sphere

# Input radius from user

import math

radius = float(input("Enter the radius of the sphere: "))

volume = (4/3) * math.pi * (radius ** 3)

print("\nVolume of the sphere = {:.2f}".format(volume))
