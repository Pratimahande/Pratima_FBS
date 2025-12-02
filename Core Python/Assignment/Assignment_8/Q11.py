# Program to check if a number is Armstrong number or NOT

def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

def is_armstrong(num):
    n = count_digits(num)  
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** n  
        temp //= 10

    if total == num:
        return True
    else:
        return False

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is NOT an Armstrong number.")

