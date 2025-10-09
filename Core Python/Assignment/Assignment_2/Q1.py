# Program to convert time (hh, mm, ss) into seconds

# Input from user

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = (hours * 3600) + (minutes * 60) + seconds

print("Total seconds =", total_seconds)
