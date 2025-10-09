# Program to find the minimum number of notes needed for a given amount

# Input amount from user

amount = int(input("Enter the amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("\nMinimum number of notes required:")

for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(f"{note} : {count}")
