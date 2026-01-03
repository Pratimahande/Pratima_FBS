def count_len_word(text):
    return {word : len(word) for word in text.split()}

str = input("enter the string : ")

print(count_len_word(str))