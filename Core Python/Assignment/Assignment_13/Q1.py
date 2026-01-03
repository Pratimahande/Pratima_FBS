#Program to Add a Key-Value Pair to the Dictionary

dict1 = {"a": 'Pratima', "b": 'Patil'}
dict2 = {"c": 'Trisha', "d": 'Patil'}

result = {**dict1, **dict2}

print(result)


#Using update()

dict1 = {"a": 'Pratima', "b": 'Patil'}
dict2 = {"c": 'Trisha', "d": 'Patil'}

result = dict1.copy()
result.update(dict2)

print(result)


#Using a Variable Key and Value#

dict1 = {"a": 'Pratima', "b": 'Patil'}
dict2 = {"c": 'Trisha', "d": 'Patil'}

result = dict1 | dict2

print(result)


# Python program to add a key-value pair to a dictionary

dict1 = {"a": 'Pratima', "b": 'Patil'}
dict2 = {"c": 'Trisha', "d": 'Patil'}

result = {}

for d in (dict1, dict2):
    for key, value in d.items():
        result[key] = value

print(result)


