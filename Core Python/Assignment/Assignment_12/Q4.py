def exchange(str):
    if(len(str)<=1):
        return str
    
    new_str = str[-1] + str[1:-1] + str[0]
    return new_str

string=input("Enter the string : ")
res=exchange(string)
print("original string : ", string)
print("exchage the char : ",res)