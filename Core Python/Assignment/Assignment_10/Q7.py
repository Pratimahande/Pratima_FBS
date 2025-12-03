def cube(li):
    cube_li=[]
    for n in li:
        cube = n * n * n
        cube_li.append(cube)
    return cube_li

num = int(input("Enter the element you have in list : "))
li=[]

for i in range(1,num+1):
    ele = int(input(f"enter the element{i} : "))
    li.append(ele)

cube_li =cube(li)
print("original list",li)
print("cube list",cube_li)