def divisible_by_any():
    return [ i for i in range(1,1001)
            if any(i % n == 0 for n in range(1,10))]

print(divisible_by_any())