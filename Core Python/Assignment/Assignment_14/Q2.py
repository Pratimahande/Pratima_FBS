# Python program to remove the intersection of a second set with a first set

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# Remove elements that are common in both sets

set1 -= set2

print("Updated first set:", set1)


#Using difference_update()

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

set1.difference_update(set2)

print(set1)



# Python program to remove the intersection of a second set with a first set

set1 = set(map(int, input("Enter elements of the first set: ").split()))
set2 = set(map(int, input("Enter elements of the second set: ").split()))

set1.difference_update(set2)

print("First set after removing intersection:", set1)
