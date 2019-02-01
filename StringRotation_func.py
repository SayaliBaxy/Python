def rotation(s1,s2):
    s3= s1+ s1
    if s2 in s3:
        print("yes")
    else:
        print("No")
    return s3
        


s1=input("enter a first string: ")
s2=input("enter a second string: ")
print(rotation(s1,s2))
