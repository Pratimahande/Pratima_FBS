# Python program to find all unique words and count their frequency 

strings = [
    "hello Data Science",
    "hello python",
    "world of python",
    "hello Artifical Intelligence"
]

# Split all strings into words

words = []
for s in strings:
    words.extend(s.split())

unique_words = set(words)

frequency = {word: words.count(word) for word in unique_words}

print("Unique Words:", unique_words)
print("Word Frequency:", frequency)
