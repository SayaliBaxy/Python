#WAP to accept 2 strings from user and check if second string is rotation of first
#Ex:manager, german

s1=input("enter a first string: ")
s2=input("enter a second string: ")
s3= s1+ s1
if s2 in s3:
    print("yes")
else:
    print("No")
    
