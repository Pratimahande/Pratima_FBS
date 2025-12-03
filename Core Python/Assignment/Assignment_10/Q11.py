def divisible_m_n(li,m,n):
    divisible_no=[]
    for i in li:
        if(i % m == 0 and i %n ==0):
            divisible_no.append(i)
    return divisible_no

original_li=[10,20,30,40,50,60,70,80,90,100]
print("original list : ",original_li)

m = int(input("enter the value of m number : "))
n = int(input("enter the value of n number : "))

res = divisible_m_n(original_li,m,n)
print(f"no divisible by {m} and {n}: {res}")
