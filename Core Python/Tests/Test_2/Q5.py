# Program to calculate total bill after adding 18% GST

p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))
p4 = float(input("Enter price of product 4: "))
p5 = float(input("Enter price of product 5: "))

total = p1 + p2 + p3 + p4 + p5

GST = total * 0.18
final_amount = total + GST

print("\nTotal amount before GST: Rs.", round(total, 2))
print("GST @18%: Rs.", round(GST, 2))
print("Total bill amount after GST: Rs.", round(final_amount, 2))
