def add (li):
    sum =0
    for i in range(0,len(li)):
        sum += li[i]
    return sum

li=[10,20,30,40,50]
print(add(li))