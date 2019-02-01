#WAP to accept two numbers from user and perform following operations:
#add, substract, divide, multiply and exponential.

a= input("enter first number:")
b= input("enter second number:")
add=int( a)+int(b)
sub=int( a)-int(b)
div=int( a)/int(b)
mul=int( a)*int(b)
exp=int(a**b)
print('The sum of numbers:', add)
print('The subtraction of numbers:',sub)
print('The division of numbers:',div)
print('The multipilcation of numbers:',mul)
print('The exponential of numbers:',exp)
