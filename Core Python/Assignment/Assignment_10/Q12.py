def cube(li):
    cube_li=[]
    for n in li:
        cube = n * n * n
        cube_li.append(cube)
    return cube_li

def square(li):
    square_li=[]
    for n in li:
        square = n * n 
        square_li.append(square)
    return square_li

num = int(input("Enter the element you have in list : "))
li=[]

for i in range(1,num+1):
    ele = int(input(f"enter the element{i} : "))
    li.append(ele)

cube_li ,square_li = square(li),cube(li)
print("original list",li)
print("cube list",cube_li)
print("square list",square_li)