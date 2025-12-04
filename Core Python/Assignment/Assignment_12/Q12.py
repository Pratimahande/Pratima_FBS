def count_lowercase(str):
    count = 0
    for ch in str:
        if ch.islower():
            count +=1
    return count

string =input("enter the string : ")

print(count_lowercase(string))