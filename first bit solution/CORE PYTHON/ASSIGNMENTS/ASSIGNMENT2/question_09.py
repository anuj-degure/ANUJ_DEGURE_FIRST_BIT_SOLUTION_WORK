# Write a program to swap two numbers without using third variable.

a=int(input('enter the value of a:'))
b=int(input('enter the value of b:'))

a=a+b
b=a-b
a=a-b

print("the value of a:",a)
print("the value of b:",b)