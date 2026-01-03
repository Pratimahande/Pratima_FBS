def count_num_space(text):

    return sum(1 for ch in text if ch ==' ')

str =input("enter the string : ")

print(count_num_space(str))