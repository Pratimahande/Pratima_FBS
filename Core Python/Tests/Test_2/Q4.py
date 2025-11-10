# Program to calculate total cost of painting 4 equal sized walls

length = float(input("Enter the length of the wall (in meters): "))
height = float(input("Enter the height of the wall (in meters): "))
cost_per_sq_m = float(input("Enter the cost of painting per square meter (in Rs): "))

total_area = 4 * length * height
total_cost = total_area * cost_per_sq_m

print("\nTotal area to be painted:", total_area, "sq. meters")
print("Total cost of painting: Rs.", round(total_cost, 2))
