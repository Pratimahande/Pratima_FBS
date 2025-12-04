def vowel(str):
    vowels="aeiouAEIOU"
    count =0
    for ch in str:
        is_vowel = False
    
        for i in vowels:
            if(ch == i):
                is_vowel = True
                break
        if (is_vowel):
            count += 1
    
    return count

string =input("Enter the string : ")
res= vowel(string)
print("total vowels : ",res)