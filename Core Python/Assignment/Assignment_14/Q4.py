# Python program to find all pairs in a list whose sum is equal to a given value

numbers = [1, 2, 3, 4, 5, 6, 7]
target_sum = 7

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_sum:
            pairs.append((numbers[i], numbers[j]))

print("Pairs with sum", target_sum, ":", pairs)


# using set

numbers = [1, 2, 3, 4, 5, 6, 7]
target_sum = 7

seen = set()
pairs = set()

for num in numbers:
    complement = target_sum - num
    if complement in seen:
        pairs.add((min(num, complement), max(num, complement)))
    seen.add(num)

print("Pairs with sum", target_sum, ":", pairs)
