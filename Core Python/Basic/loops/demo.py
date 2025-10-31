def check_special_three_digit_number():
    while True:
        try:
            number = int(input("Enter a 3-digit number: "))
            if 100 <= number <= 999:
                # Extract digits
                first = number // 100
                second = (number // 10) % 10
                third = number % 10

                # Check the conditions
                if first == 2 * second and first == third / 2:
                    print("Yes, you have done it!")
                else:
                    print("Please try next time.")
                break
            else:
                print("Invalid input. Enter a 3-digit number (100 to 999).")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

# Run the program
check_special_three_digit_number()


    