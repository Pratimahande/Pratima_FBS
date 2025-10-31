# Program to print all Armstrong numbers in a given range

first = int(input("Enter the first number: "))
last = int(input("Enter the last number: "))

print(f"Armstrong numbers between {first} and {last} are:")

for num in range(first, last + 1):
    # Find the number of digits
    order = len(str(num))
    
    # Calculate the sum of powers of digits
    sum_of_powers = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** order
        temp //= 10
    
    # Check if the number is an Armstrong number
    if num == sum_of_powers:
        print(num, end=" ")