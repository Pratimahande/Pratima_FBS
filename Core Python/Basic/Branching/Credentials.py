#Credentials in python

uid = 'u123'
passw = 'user@123'

user_id = input("Enter username:")
user_passw =input("Enter password:")


if(user_id == uid and user_passw == passw):
    print("login successfully.")

else:
    print("wrong username or password.")
        
 #ifelselader

n=int(input("Enter number:"))

if(n==0):
    print(f'{n}is a neutral number.')

elif(n>0):
    print(f'{n}is a positive number.')

else:
    print(f'{n}is a negative number.')              



