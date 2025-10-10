#IfElseLadder

n=int(input("Enter number:"))
if(n==0):
    print(f'{n} is a neutral number.')
elif(n>0):
    print(f'{n} is a positive number.' )
else:
    print(f'{n} is a negative number.')
    