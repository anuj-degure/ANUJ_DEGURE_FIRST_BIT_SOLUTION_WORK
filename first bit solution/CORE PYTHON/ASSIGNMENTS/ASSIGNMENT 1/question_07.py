# Program to Find the Roots of a Quadratic Equation

import math
a=int(input('entre the value of a:'))
b=int(input('entre the value of b:'))
c=int(input('entre the value of c:'))

d=a*c
e=4*d
f=(b**2)
g=f-e
h=math.sqrt(g)
i=(-b)
j=i+h
k=i-h
l=2*a
m=j/l
n=k/l

print('the root of the quadratic equation is:',n)