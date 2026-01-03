# Python program to find all unique combinations of 3 numbers

numbers = [1, 2, -1, 0, 2, -2, 3]
target = 3

numbers.sort()
triplets = set()

n = len(numbers)

for i in range(n - 2):
    left = i + 1
    right = n - 1
    
    while left < right:
        total = numbers[i] + numbers[left] + numbers[right]
        
        if total == target:
            triplets.add((numbers[i], numbers[left], numbers[right]))
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1

print("Unique triplets adding to", target, ":", triplets)



# using unique set 
numbers = [1, 2, -1, 0, 2, -2, 3]
target = 3

triplets = set()

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:
                triplets.add(tuple(sorted([numbers[i], numbers[j], numbers[k]])))

print(triplets)
