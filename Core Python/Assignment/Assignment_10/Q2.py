def min_max(li):
    min_val = li[0]
    max_val = li[0]
    for i in li[1:]:
        if i > max_val:
            max_val = i
        elif i < min_val:
            min_val = i
    return max_val, min_val

li = [12, 3, 56, 78, 0, 90, 44]
max_val, min_val = min_max(li)
print("maximum and minimum of the list =", max_val, "and", min_val)

