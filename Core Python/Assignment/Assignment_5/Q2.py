# Program to students accept marks of 5 subject marks from user calculate percentage

num_std = int(input("Enter number of students: "))
total_percentage = 0

for i in range(1, num_std + 1):
    print(f"\nEnter marks for Student {i}:")
    
    # Take 5 subject marks
    total_marks = 0
    for j in range(1, 6):
        mark = float(input(f"  Enter marks for subject {j}: "))
        total_marks += mark
    
    percentage = (total_marks / 500) * 100
    print(f" Percentage of Student {i}: {percentage:.2f}%")
    
    total_percentage += percentage

# Calculate and display average percentage
average_percentage = total_percentage / num_std
print(f"\nAverage percentage of all students: {average_percentage:.2f}%")