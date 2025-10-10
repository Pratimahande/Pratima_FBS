# Program to check whether an alphabet is vowel or consonant

# Accept a single alphabet from user

ch = input("Enter any alphabet: ")

if ch.isalpha() and len(ch) == 1:
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(f"{ch} is a Vowel.")
    else:
        print(f"{ch} is a Consonant.")
else:
    print("Please enter a valid single alphabet.")
