num = int(input("Enter the element you have in list : "))
li=[]

for i in range(1,num+1):
    ele = int(input(f"enter the element{i} : "))
    li.append(ele)
print(li)

search_ele=int(input("enter the element you have search in list : "))
count = 0

for x in li:
    if(x == search_ele):
        count += 1

if (count > 0):
    print(search_ele,"present in list.")
    print(search_ele,f'is {count} time')
else:
    print(search_ele,"is not present in list.")