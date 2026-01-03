# Python program to find the longest common prefix using set

def longest_common_prefix(strings):
    if not strings:
        return ""

    # Find the shortest string 

    shortest_str = min(strings, key=len)

    lcp = ""
    for i in range(len(shortest_str)):
        chars_at_pos = {s[i] for s in strings}  
        if len(chars_at_pos) == 1:  
            lcp += shortest_str[i]
        else:
            break

    return lcp

strings = ["flower", "flow", "flight"]
result = longest_common_prefix(strings)
print("Longest Common Prefix:", result)
