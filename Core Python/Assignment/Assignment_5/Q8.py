ch = 0
while( ch != '6' ):
    print('''please selsect your option :
        1.factorial
        2.exponent
        3.sum of geometric series from 1 to n
        4.s= a + a2/2+a3/3.....a10/10
        5. x-x2/3+x3/5-x4/7......n
        6.EXIT..
          .....''')
    ch = input("ENTER YOUR CHOICE : ")
    if(ch == '1'):
        print("########FACTORIAL##########")
        n = int (input("ENTER THE NUMBER U HAVE FACTORICAL OF : "))
        fact =1
        for i in range(1,n+1):
            fact *=i
            print(f" FACT OF {n} IS : {i}")
        print(f" FACTORIAL OF {n} IS :{fact}") 


    elif( ch == '2'):
        print(f"########EXPONENT##########")
        num = int(input("ENTER THE NUMBER U HAVE exponent :"))
        total =0

        for i in range(1,num+1):
            total += num ** i
            print(f"EXPONENT = {i} of {num}")
        print(f" EXPONTN OF {num} IS :{total}")
        

    elif( ch == '3'):
        print(f"######## sum of geometric series from 1 to n ##########")
        n = int(input("enter the number of term :"))
        if(n <= 0):
            print("positive intiger for n:")
        else:
            total = 0
            for i in range(1,n+1):
                term= 2 **(i-1)
                total += term
                print(f" 2^{i-1} = {term}")
            sum = 2 ** n-1
            print(f" sum of serirs of geometric is = {sum}")


    elif( ch == '4'):
        print(f"###### s= a + a2/2+a3/3.....a10/10 ##########")
        n =  int(input("ENTER THE NUMBER : "))
        S = 0
        for i in range(1,n+1):
            S += (n** i)/i
        print(f"sum of series = {S}")

    elif( ch == '5'):
        print(print(f"######## x-x2/3+x3/5-x4/7......n ##########"))
        x= int(input("enter the x value : "))
        n = int(input("ENTER THE NUMBER : "))
        S=0
        sign = 1
        den =1
        for i in range(1,n+1):
            term = sign *(x ** i) /den
            S += term
            sign *= -1
            den +=2
        print(f"sum of series = {term}")

              
    else:
        print(f"INVALID CHOICE.")
