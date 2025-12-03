def remove_even(even_no):
    even_li=[]
    for i in even_no:
        if(i%2 != 0):
            even_li.append(i)
    return even_li

li=[1,2,3,4,5,6,7,8,9,10]
print("original list:",li)

res= remove_even(li)
print("after removing even numbers : ",res)