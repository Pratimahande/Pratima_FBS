# Program to calculate total amount to ticket (given condition)

num_passengers = int(input("Enter number of passengers: "))

ticket_cost = float(input("Enter cost per ticket: "))
total_amount = 0

for i in range(1, num_passengers + 1):
    age = int(input(f"Enter age of passenger {i}: "))

    # Apply discount based on age
    if age < 12:
        discount = 0.30  # 30% discount
    elif age > 59:
        discount = 0.50  # 50% discount
    else:
        discount = 0.0   # no discount

    final_cost = ticket_cost * (1 - discount)
    print(f"  Ticket cost for passenger {i}:  ₹{final_cost:.2f}")

    total_amount += final_cost

# Display total ticket amount
print(f"\nTotal amount to be paid for all passengers:  ₹{total_amount:.2f}")