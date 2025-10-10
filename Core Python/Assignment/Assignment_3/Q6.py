# Program to calculate Profit or Loss

# Input cost price and selling price

cp = int(input("Enter Cost Price (CP): "))
sp = int(input("Enter Selling Price (SP): "))

# Check for profit or loss

if sp > cp:
    profit = sp - cp
    print(f" Profit = Rs. {profit:.2f}")
elif cp > sp:
    loss = cp - sp
    print(f" Loss = Rs. {loss:.2f}")
else:
    print("No Profit, No Loss.")
