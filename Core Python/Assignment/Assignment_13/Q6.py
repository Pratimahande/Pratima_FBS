#Program to Multiply All the Items in a Dictionary

#Using a Loop

my_dict = {'a': 10, 'b': 20, 'c': 30}

result = 1
for value in my_dict.values():
    result *= value

print("Product of all items:", result)



#Using math.product()

import math

my_dict = {'a': 1, 'b': 8, 'c': 4}

result = math.prod(my_dict.values())

print("Product of all items:", result)


# Python program to multiply all the items in a dictionary

my_dict = {"x": 10, "y": 20, "z": 30}

product = 1
for value in my_dict.values():
    product *= value

print("Product:", product)