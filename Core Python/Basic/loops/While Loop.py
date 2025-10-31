def is_leap_year(year):
    if year % 4 != 0:
        return False  # Not divisible by 4
    elif year % 100 != 0:
        return True   # Divisible by 4, but not by 100
    elif year % 400 != 0:
        return False  # Divisible by 100 but not by 400
    else:
        return True   # Divisible by 400

# Example usage
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")



