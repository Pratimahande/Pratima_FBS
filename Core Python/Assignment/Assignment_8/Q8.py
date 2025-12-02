# Program to find reverse of a number

def reverse_number(num):
    reverse = 0
    while num > 0:
        digit = num % 10           
        reverse = (reverse * 10) + digit  
        num //= 10                 
    return reverse

number = int(input("Enter a number: "))
result = reverse_number(number)
print("The reverse of the number is:", result)
