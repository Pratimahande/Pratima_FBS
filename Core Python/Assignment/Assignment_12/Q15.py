def length(str):
    count = 0
    for ch in str :
        count +=1
    return count

def lager_string(s1,s2):
    len1 =length(s1)
    len2 =length(s2)

    if(len1> len2):
        return s1
    elif(len1< len2):
        return s2
    else:
        return "both strings are equale"

string1 = input("enter the string 1 :")
string2 =input("enter the string 2 :")

print(lager_string(string1,string2))