def remove_Occurance(original_li,ele):
    li=[]

    for i in original_li:
        if (i != ele):
            li.append(i)
    return li

n=[10,27,89,65,45,10,32,78]
print("original list:",n)
val = int(input("enter the value to be remove : "))

res= remove_Occurance(n,val)
print("removing of occurance no",val,":",res)