# Program to calculate cost of painting building walls (interior and exterior)

area_one_wall = float(input("Enter area of one wall (in sq. meters): "))
cost_interior = float(input("Enter cost per sq. meter for interior wall: "))
cost_exterior = float(input("Enter cost per sq. meter for exterior wall: "))


num_interior_walls = 8
num_exterior_walls = 7

total_interior_area = num_interior_walls * area_one_wall
total_exterior_area = num_exterior_walls * area_one_wall

interior_cost = total_interior_area * cost_interior
exterior_cost = total_exterior_area * cost_exterior
total_cost = interior_cost + exterior_cost

print("\n--- Painting Cost Calculation ---")
print("Total Interior Area =", total_interior_area, "sq.m")
print("Total Exterior Area =", total_exterior_area, "sq.m")
print("Cost for Interior Walls = ₹", interior_cost)
print("Cost for Exterior Walls = ₹", exterior_cost)
print("Total Painting Cost = ₹", total_cost)
