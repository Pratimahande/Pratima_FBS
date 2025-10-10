# Program to calculate total ticket amount for 5 people based on age and discount

total_amount = 0  

# Loop for 5 people

for i in range(1, 6):
    print(f"\nPerson {i}:")
    age = int(input("Enter age: "))
    ticket_price = float(input("Enter ticket amount per person: "))
    if age < 12:
        discount = 0.30 * ticket_price  
        final_price = ticket_price - discount
    elif age > 59:
        discount = 0.50 * ticket_price  
        final_price = ticket_price - discount
    else:
        final_price = ticket_price
    print(f"Ticket after discount: Rs. {final_price:.2f}")
    total_amount += final_price

print("\n-------------------")
print(f"Total ticket amount for 5 people = Rs. {total_amount:.2f}")
print("--------------------")
