# Write a program to enter P, T, R and calculate simple Interest.

principal_amount=int(input('enter the principal amount:'))
rate_of_intrest=int(input('enter the rate of interst:'))
time=int(input('enter the time taken(in years):'))

simple_intrest=((principal_amount*rate_of_intrest*time)/100)

print('the simple interst of your amount is:',simple_intrest)