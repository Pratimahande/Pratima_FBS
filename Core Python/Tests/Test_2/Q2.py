# Accept a 3-digit number from the user

num = int(input("Enter a 3-digit number: "))

if 100 <= num <= 999:
    first = num // 100
    second = (num // 10) % 10
    third = num % 10

    if first == 2 * second and first * 2 == third:
        print("Yes, you have done it")
    else:
        print("Please try next time")
else:
    print("Please enter a valid 3-digit number")
