def remove_Duplicate(li):
    single_li =[]

    for i in li:
        if i not in single_li:
            single_li.append(i)
    return single_li
        
num = int(input("Enter the element you have in list : "))
li=[]

for i in range(1,num+1):
    ele = int(input(f"enter the element{i} : "))
    li.append(ele)

single_li=remove_Duplicate(li)
print("original list:",li)
print("removing duplicate elements from list :",single_li) 