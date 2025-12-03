li =[10,20,30,40,50,60,70,80,90,100]

rev_li =[]

i = len(li)-1
while(i>=0):
    rev_li.append(li[i])
    i=i-1

print("original list:",li)
print("reversed list :",rev_li)

li = [10,20,30,40,50,60,70,80,90,100]
print(li[::-1])