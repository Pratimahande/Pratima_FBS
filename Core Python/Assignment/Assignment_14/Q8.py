# Python program to group anagrams from a given list of strings

strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram_groups = {}

for word in strings:
    key = ''.join(sorted(word))
    
    if key in anagram_groups:
        anagram_groups[key].append(word)
    else:
        anagram_groups[key] = [word]

result = list(anagram_groups.values())
print("Grouped Anagrams:", result)



#Using defaultdict

from collections import defaultdict

strings = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = defaultdict(list)

for word in strings:
    groups[''.join(sorted(word))].append(word)

print(list(groups.values()))
