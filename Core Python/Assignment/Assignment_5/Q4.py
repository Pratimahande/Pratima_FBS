# Program to check if given number is armstrong number or not

num = int(input("Enter a number: "))
original_num = num

num_digits = len(str(num))

sum_of_powers = 0

while num > 0:
    digit = num % 10               
    sum_of_powers += digit ** num_digits  
    num //= 10                     

# Check if Armstrong or not
if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is NOT an Armstrongnumber.")