def even_odd(li):
    even_li=[]
    odd_li=[]

    for i in li:
        if(i % 2 ==0):
            even_li.append(i)
        else:
            odd_li.append(i)
    return even_li, odd_li

li=[]
num = int(input("Enter the element you have in list : "))
for i in range(1,num+1):
    ele = int(input(f"enter the element{i} : "))
    li.append(ele)

even_li, odd_li = even_odd(li)

print("original list:",li)
print("even list : ",even_li)
print("odd list : ",odd_li)