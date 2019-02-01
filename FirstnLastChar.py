#WAP to accept string from user and return a string having first 2 and last 2
#characters of input string.  Example input = spring then output = spng

s= raw_input("enter any string : ")
s1 = (s[0]+s[1])+(s[-2]+s[-1])
print(s1)
