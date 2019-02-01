n= input("enter number between 1 to 4")
while n<4:
    i = input("enter the operation to be performed: Add,sub,div or mul:")
    if i=='add':
        a,b = input("enter any two numbers")
        c=a+b
        print("The addition of two numbers is: "+str(c))
    elif i=='sub':
        a,b = str(input("enter any two numbers"))
        c=a-b
        print("The substraction of two numbers is: "+str(c))
    elif i=='div':
        a,b = str(input("enter any two numbers"))
        c=a/b
        print("The division of two numbers is: "+str(c))
    elif i=='mul':
        a,b = str(input("enter any two numbers"))
        c=a*b
        print("The multiplication of two numbers is: "+str(c))
    else:
        print("Entered operation does not exist")
    
        



  
