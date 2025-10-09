# Program to convert distance from kilometers to meters and centimeters

km = float(input("Enter distance in kilometers: "))

# Conversions
meters = km * 1000          # 1 km = 1000 meters
centimeters = km * 100000   # 1 km = 100000 centimeters


print("Distance in meters =", meters)
print("Distance in centimeters =", centimeters)
