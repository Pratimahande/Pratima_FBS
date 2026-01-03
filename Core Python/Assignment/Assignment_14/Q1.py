# Python program to find elements in a given set that are not in another set

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

difference = set1 - set2   

print("Elements in set1 not in set2:", difference)


#Using difference()

difference = set1.difference(set2)
print(difference)


# Python program to find elements in a given set that are not in another set

set1 = set(map(int, input("Enter elements of first set: ").split()))
set2 = set(map(int, input("Enter elements of second set: ").split()))

result = set1 - set2

print("Elements in the first set but not in the second:", result)
