def main():
    s= input("enter a string")
    print("The palindrome is:"+ str(palindrome(s)))    


def palindrome(s):
    if s[::1]==s[::-1]:
        print("String is a palindrome")
    else:
        print("string is not a palindrome")
    return s


if __name__=='__main__':
    main()

