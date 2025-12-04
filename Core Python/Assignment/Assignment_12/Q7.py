def length_string(str):
    len = 0
    for _ in str:
        len +=1
    return len

string = "Hello I am Pratima"

res = length_string(string)

print("original string : ",string)
print("length of string : ",res)