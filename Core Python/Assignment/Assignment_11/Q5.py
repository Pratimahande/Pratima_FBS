def bubble_Sort(li):
    size = len(li)
    for i in range(1,size):
        for j in range(0,size - 1 ):

            if(li[j] > li[j + 1]):
                li[j] , li[j + 1] = li[j + 1] , li[j]
    return li

num = int(input("Enter the element you have in list : "))
li=[]

for i in range(1,num+1):
    ele = int(input(f"enter the element {i} : "))
    li.append(ele)

print("original list:",li)
res=bubble_Sort(li)
print(f"sorted list by len {i}:",res)