# Find the sum of three-digit number.
 
number=int(input('enter the three digit number:'))

a=number//100
b=(number%100)//10
c=((number%100)%10)//1
d=a+b+c

print('the sum of your three digit number is:',d)