# Program to find sum of digits of a number

def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10      
        total += digit       
        num //= 10            
    return total

number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("The sum of digits of", number, "is:", result)
