# Program to calculate area of rectangle

def area_of_rectangle(length, breadth):
    area = length * breadth
    return area

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = area_of_rectangle(length, breadth)
print("The area of the rectangle is:", area)
