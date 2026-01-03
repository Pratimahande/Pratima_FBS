# Python program to count the frequency of words in a string using a dictionary

text = input("Enter a string: ")

words = text.split()

freq = {}

# Count frequency

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequency:")
print(freq)
