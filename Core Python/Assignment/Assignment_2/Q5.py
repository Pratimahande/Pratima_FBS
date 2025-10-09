# Program to calculate selling price of a book

# Input cost price and discount percentage from user

cost_price = int(input("Enter the cost price of the book: "))
discount_percent = int(input("Enter the discount percentage: "))

discount_amount = (discount_percent / 100) * cost_price

selling_price = cost_price - discount_amount

print("\nCost Price =", cost_price)
print("Discount Amount =", discount_amount)
print("Selling Price =", selling_price)
