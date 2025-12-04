def count_digit_letter(str):
    digit_count = 0
    letter_count = 0

    for ch in str:
        if('0'<= ch <= '9'):
            digit_count +=1
        elif ('A' <= ch <='Z')or('a' <=ch <='z'):
            letter_count += 1

    return letter_count,digit_count

string = input("enter the string : ")
digit,letter =count_digit_letter(string)

print("digit : ",digit)
print("letter : ",letter)