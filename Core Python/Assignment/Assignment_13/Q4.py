# Python program to generate a dictionary 

n = int(input("Enter a number: "))

result = {}

for x in range(1, n + 1):
    result[x] = x * x

print(result)


# containing numbers between 1 and n in the form (x, x*x)

n = int(input("Enter a number: "))
result = {x: x*x for x in range(1, n + 1)}
print(result)