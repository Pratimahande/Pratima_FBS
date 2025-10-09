# Program to calculate percentage of a student based on marks of 5 subjects

# Input marks for 5 subjects

sub1 = int(input("Enter marks of Subject 1: "))
sub2 = int(input("Enter marks of Subject 2: "))
sub3 = int(input("Enter marks of Subject 3: "))
sub4 = int(input("Enter marks of Subject 4: "))
sub5 = int(input("Enter marks of Subject 5: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5

maximum_marks = 500

percentage = (total_marks / maximum_marks) * 100

print("\nTotal Marks =", total_marks)
print("Percentage = {:.2f}%".format(percentage))
