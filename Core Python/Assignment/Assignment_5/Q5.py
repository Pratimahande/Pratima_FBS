# Program to accept in integer amount from user tell minimum number notes(Using looping to optimize the problem)
amount = int(input("Enter the amount: "))

# List of available denominations (in descending order)
denominations = [2000, 1000, 500, 200, 100, 50, 20, 10]

# Dictionary to store count of notes for each denomination
note_count = {}

remaining_amount = amount

# Loop through each denomination
for note in denominations:
    if remaining_amount >= note:
        count = remaining_amount // note  
        remaining_amount = remaining_amount % note
        note_count[note] = count

# Display results
print(f"\nMinimum notes required for ₹{amount}:")

total_notes = 0
for note, count in note_count.items():
    print(f"₹{note} x {count}")
    total_notes += count

print(f"\nTotal number of notes:{total_notes}")