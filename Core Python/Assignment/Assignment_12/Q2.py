def remove_char(str,n):
    return str[:n] + str[n+1:]

str= input("enter the string : ")
n=int(input("which index of string : "))
res =remove_char(str,n)

print("original string : ",str)
print(f"After the removing char : {n} of",res)