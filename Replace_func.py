def Replace(s):
    s1=s[0]+s[1:].replace(s[0],'*')
    return s1

s=input("enter any string")
print(Replace(s))

