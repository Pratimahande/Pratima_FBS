# Program to find reverse the number using recursive function

def reverse_num(n, rev=0):
    if n == 0:
        return rev
    else:
        digit = n % 10
        rev = rev * 10 + digit
        return reverse_num(n // 10, rev)

num = int(input("Enter any number: "))
result = reverse_num(num)
print("Reversed number =", result)
