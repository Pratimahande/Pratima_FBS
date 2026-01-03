# Python program to find two numbers whose product is maximum using set

numbers = [1, -10, 2, 6, -7, 5, 2]

unique_numbers = list(set(numbers))

max_product = float('-infinity')
pair = ()

for i in range(len(unique_numbers)):
    for j in range(i + 1, len(unique_numbers)):
        product = unique_numbers[i] * unique_numbers[j]
        if product > max_product:
            max_product = product
            pair = (unique_numbers[i], unique_numbers[j])

print("Pair with maximum product:", pair)
print("Maximum product:", max_product)
