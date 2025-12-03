def li_union(li1,li2):
    union_li=[]
    for i in li1:
        if(i not in union_li):
            union_li.append(i)

    for i in li2:
        if(i not in union_li):
            union_li.append(i)
    return union_li

num = int(input("Enter the element you have in list : "))
li1=[]

for i in range(1,num+1):
    ele = int(input(f"enter the element {i} : "))
    li1.append(ele)
    
num2 = int(input("Enter the element you have in list : "))
li2=[]

for i in range(1,num2+1):
    ele = int(input(f"enter the element {i} : "))
    li2.append(ele)

res =li_union(li1,li2)
print("list 1 : ",li1)
print("list 2 : ",li2)
print("union element of list : ",res)