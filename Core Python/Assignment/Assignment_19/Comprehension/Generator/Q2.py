def palindrom_no():
    num =0
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num +=1

res = palindrom_no()
print(next(res))
print(next(res))
print(next(res))
print(next(res))