n=str(input("enter any number"))
if n[::1]==n[::-1]:
    print("Entered number is a palindrome")
else:
    print("Entered number is not a palindrome")
