def space(str):
    new_str = ""
    for ch in str:
        if(ch == " "):
            new_str += "--"
        else:
            new_str += ch
    return new_str
string = "Hi I am Pratima"

res = space(string)
print("modified string : ",res)