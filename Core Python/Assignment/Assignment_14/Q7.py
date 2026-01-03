# Python program to find missing numbers between two sets using set operations

set1 = {1, 2, 3, 4, 5, 10}
set2 = {3, 4, 5, 6, 7, 8}

missing_in_set2 = set1 - set2

missing_in_set1 = set2 - set1

print("Numbers in set1 but missing in set2:", missing_in_set2)
print("Numbers in set2 but missing in set1:", missing_in_set1)


#with User Input

set1 = set(map(int, input("Enter numbers for first set: ").split()))
set2 = set(map(int, input("Enter numbers for second set: ").split()))

missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("Missing in second set compared to first:", missing_in_set2)
print("Missing in first set compared to second:", missing_in_set1)

