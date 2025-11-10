import math

r = 20     
length = 50
breadth = 40
cost_per_m = 35

perimeter = (2 * length) + breadth + (math.pi * r)

total_wire_length = 5 * perimeter
total_cost = total_wire_length * cost_per_m

print("Total length of wire needed:", total_wire_length, "m")
print("Total cost of fencing: Rs.", round(total_cost, 2))
