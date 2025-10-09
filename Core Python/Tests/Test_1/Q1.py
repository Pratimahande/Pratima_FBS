length = int (input("enter the value os length : "))
breath = int (input("enter the value os breath : "))
radius = int (input("enter the value os radius : "))

area_rectangle = length *  breath
perimeter_rectangle = 2 *(length * breath)

area_circle = (3.14 * radius * radius) 
perimeter_circle = 2 *(3.14 * radius)

print(f" area of rectangle {length} , {breath} is {area_rectangle} and peimeter of rectangle is {perimeter_rectangle}")
print(f"area of circle of {radius} is {area_circle} and perimeter of circle is {perimeter_circle}")