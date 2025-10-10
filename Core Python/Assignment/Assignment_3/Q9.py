# Program to calculate grade based on marks of 5 subjects

# Input marks for 5 subjects

s1 = int(input("Enter marks of Subject 1: "))
s2 = int(input("Enter marks of Subject 2: "))
s3 = int(input("Enter marks of Subject 3: "))
s4 = int(input("Enter marks of Subject 4: "))
s5 = int(input("Enter marks of Subject 5: "))

total = s1 + s2 + s3 + s4 + s5
percentage = (total / 500) * 100

print(f"\nTotal Marks = {total}")
print(f"Percentage = {percentage:.2f}%")

if percentage >= 75:
    print("Grade: Distinction")
elif percentage >= 60:
    print("Grade: First Class")
elif percentage >= 50:
    print("Grade: Second Class")
elif percentage >= 40:
    print("Grade: Pass Class")
else:
    print("Grade: Fail")
