#WAP to accept 3 numbers from the user and print the minimum out of them.

a,b,c= input("enter any 3 numbers")
if a<b and a<c:
    print("a is minimum")
elif b<a and b<c:
    print("b is minimum")
else:
    print("c is minimum")
