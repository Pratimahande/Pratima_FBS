#Program to Check if a Given Key Exists in a Dictionary or Not

#Using the in operator#

my_dict = {"name": "Pratima", "age": 26, "city": "Kolhapur"}
key = "age"
# Check if key exists
if key in my_dict:
    print(f"Key '{key}' exists in the dictionary.")
else:
    print(f"Key '{key}' does NOT exist in the dictionary.")



#Using dict.get()

key = "employee"

if my_dict.get(key) is not None:
    print(f"Key '{key}' exists in the dictionary.")
else:
    print(f"Key '{key}' does NOT exist in the dictionary.")



#Using keys() method

key = "city"

if key in my_dict.keys():
    print(f"Key '{key}' exists in the dictionary.")
else:
    print(f"Key '{key}' does NOT exist in the dictionary.")



