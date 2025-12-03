def li_intersection(li1,li2):
    inner_li=[]
    for i in li1:
        if(i in li2 and i not in inner_li):
            inner_li.append(i)

    return inner_li

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

res =li_intersection(li1,li2)
print("list 1 : ",li1)
print("list 2 : ",li2)
print("intersection element of list : ",res)