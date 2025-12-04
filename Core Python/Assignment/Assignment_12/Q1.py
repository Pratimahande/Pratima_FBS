def replace_dollar(str):
    res =""
    for ch in str:
        if(ch=='a'):
            res += '$'
        else:
            res += ch
    return res

string="banana is a fruit"
modified =replace_dollar(string)
print("original string : ",string)
print("modified string : ",modified)
