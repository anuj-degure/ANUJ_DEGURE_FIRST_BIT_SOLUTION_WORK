# Write a program to convert days into years, weeks and days

days=int(input('enter your days:'))

# into years
a=days//365

# into months
b=(days%365)//30

# into weeks
c=((days%365)%30)//4

# into days
d=((days%365)%12)//7

print('your days into years:',a)
print('month:',b)
print('week:',c)
print('days:',d)
