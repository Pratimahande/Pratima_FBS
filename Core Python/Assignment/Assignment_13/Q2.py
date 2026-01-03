#Program to Concatenate Two Dictionaries Into One

#Using Update() method

dict1 = {"Trisha": 1, "Satish": 2}
dict2 = {"Praju": 3, "Pratima": 4}

dict1.update(dict2)
print(dict1)


#Using ** operator

dict2 = {"Praju": 3, "Pratima": 4}

result = dict1 | dict2
print(result)


# Python program to concatenate two dictionaries into one

dict1 = {"Trisha": "Patil", "age": 21}
dict2 = {"city": "Pune", "country": "Indian"}

# Concatenate dictionaries

merged_dict = {**dict1, **dict2}

print("Merged dictionary:", merged_dict)


