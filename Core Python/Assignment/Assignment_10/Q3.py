def sec_Max(li):
    max = li[0]
    second_Max= 0

    for i in range(len(li)):
        if( max < li[i]):
            second_Max = max
            max = li[i]

        elif(second_Max < li[i]):
            second_Max = li[i]
            
    return second_Max

li = [56, 23, 89, 98, 45, 12, 77]
print(sec_Max(li))