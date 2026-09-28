# WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.

salary_of_employee=float(input('enter the total salary of the employee:'))
da=(salary_of_employee*10)/100
ta=(salary_of_employee*12)/100
hra=(salary_of_employee*15)/100

salary_of_employee=salary_of_employee + da + ta + hra 

print('the salary of employee adding da,ta,hra is:',salary_of_employee)