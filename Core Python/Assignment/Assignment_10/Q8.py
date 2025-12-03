def duplicate_li(li):
    du_li=[]
    for i in li:
        du_li.append(i)
    return du_li
    
li=[ 10,20,30,40,50]
duplicate = duplicate_li(li)

print("original list : ",li)
print("duplicate list : ",duplicate)

print("original list memory add : ",id(li))
print("duplicate list memory add : ",id(duplicate))