def bubble_Sort(li):
    size = len(li)
    for i in range(1,size):
        for j in range(0,size - 1 ):

            if(li[j] > li[j + 1]):
                li[j] , li[j + 1] = li[j + 1] , li[j]
    return li

def sec_Max(li):
    sorted_li = bubble_Sort(li)
    return sorted_li[-2]

num = int(input("Enter the element you have in list : "))
li=[]

for i in range(1,num+1):
    ele = int(input(f"enter the element{i} : "))
    li.append(ele)

res = sec_Max(li)
print("sorted list:",bubble_Sort(li))
print("2nd lagerest element :",res)