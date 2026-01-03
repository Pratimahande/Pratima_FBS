def remove_vowels(text):
    
    vowel = 'aeiouAEIOU'
    return ''.join([ch for ch in text if ch not in vowel ])

str = input("enter the string : ")

print(remove_vowels(str))