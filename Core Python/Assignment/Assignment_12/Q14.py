def count_words(text):
    words = text.lower().split()
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

sentence = "This is a test. This test is simple"
result = count_words(sentence)

print("Word occurrences:")
for word, count in result.items():
    print(word, ":", count)
