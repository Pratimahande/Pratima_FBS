#Program to Remove the Given Key from a Dictionary

#Using pop()

my_dict = {"fruits": 2, "flower": 2, "vegetable": 3}

key_to_remove = "flower"

my_dict.pop(key_to_remove, None)  

print(my_dict)


#Using delete()

my_dict = {"fruits": 2, "flower": 2, "vegetable": 3}

key_to_remove = "fruits"

if key_to_remove in my_dict:
    del my_dict[key_to_remove]

print(my_dict)


#Using Dictionary Comprehension

my_dict = {"fruits": 2, "flower": 2, "vegetable": 3}
key_to_remove = "vegetable"

new_dict = {k: v for k, v in my_dict.items() if k != key_to_remove}

print(new_dict)



# Python program to remove a given key from a dictionary

my_dict = {"name": "Pratima", "age": 26, "city": "Kolhapur"}

key_to_remove = input("Enter key to remove: ")

if key_to_remove in my_dict:
    my_dict.pop(key_to_remove)
    print("Updated dictionary:", my_dict)
else:
    print("Key not found in the dictonary.")
