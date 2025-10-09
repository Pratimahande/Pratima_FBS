# Program to convert distance given in feet and inches into meters and centimeters

# Input distance in feet and inches

feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))

total_meters = (feet * 0.3048) + (inches * 0.0254)

total_centimeters = total_meters * 100

print("\nDistance in meters =", round(total_meters, 2))
print("Distance in centimeters =", round(total_centimeters, 2))
