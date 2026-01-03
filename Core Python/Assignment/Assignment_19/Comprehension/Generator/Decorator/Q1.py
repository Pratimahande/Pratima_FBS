def memorization(fun):
    cache ={}
    def warpper(n):
        if(n in cache):
            print(" output is avilable..")
            return cache[n]
        output=fun(n)
        cache[n]=output
        print("output not avilable..")
        return output
    return warpper

@memorization
def fact(n):
    f=1
    for i in range(1,n+1):
        f*= i
    return f

res=fact(10)
print(f'fact of 6 is',res)
print('################')
res=fact(2)
print(res)
print('################')
res=fact(4)
print(res)
