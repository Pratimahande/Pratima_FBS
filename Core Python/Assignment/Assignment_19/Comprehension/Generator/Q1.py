def fibonacci(limit):
    a=0
    b=1
    while( a<=limit):
        yield a
        a,b =b,a+b

fib = fibonacci(5)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
