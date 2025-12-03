def mearge_sort_li(li1,li2):
    mearge = li1 + li2
    size = len(mearge)
    for i in range(1,size):
        for j in range(0,size - 1 ):

            if(mearge[j] > mearge[j + 1]):
                mearge[j] , mearge[j + 1] = mearge[j + 1] , mearge[j]
    return mearge

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

res =mearge_sort_li(li1,li2)
print("list 1 : ",li1)
print("list 2 : ",li2)
print("mearge and sorted of list : ",res)