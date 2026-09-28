# Write a program to enter P, T, R and calculate Compound Interest

principal_amount=int(input('enter the principal amount:'))
rate_of_intrest=int(input('enter the rate of interst:'))
time=int(input('enter the time taken:'))
a=(rate_of_intrest/100)
b=1+a
c=b**time
d=principal_amount*c
compound_intrest=d

print('compound intrest will be:', compound_intrest)

