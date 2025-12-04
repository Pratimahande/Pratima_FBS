def larger_str(s1,s2):
    if(len(s1) > len(s2)):
        return s1
    elif(len(s1) < len(s2)):
        return s2
    else:
        return " both are equale."
    
string1 = input("enter the string 1 :")
string2 =input("enter the string 2 :")

print(larger_str(string1,string2))