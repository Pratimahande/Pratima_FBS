#Python Program to Sum All the Items in a Dictionary

#using sum()

my_dict = {'a': 10, 'b': 20, 'c': 30}

total = sum(my_dict.values())

print("Sum of all items:", total)


#using loop

my_dict = {'a': 10, 'b': 20, 'c': 30}

total = 0
for value in my_dict.values():
    total += value

print("Sum of all items:", total)


# Python program to sum all the items in a dictionary

my_dict = {"x": 5, "y": 15, "z": 25}

total_sum = sum(my_dict.values())

print("Total sum:", total_sum)

