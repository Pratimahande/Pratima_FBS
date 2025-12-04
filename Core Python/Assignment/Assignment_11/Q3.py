def sort_by_second_element(li):
    li.sort(key=lambda x: x[1])
    return li

list = [[20,5], [60, 1], [30, 4], [10, 2]]

print("Original List:", list)

sorted_list = sort_by_second_element(list)

print("Sorted List:", sorted_list)
