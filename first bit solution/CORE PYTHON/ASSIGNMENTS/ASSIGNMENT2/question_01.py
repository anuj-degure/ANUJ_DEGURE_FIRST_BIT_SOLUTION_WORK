# convert the time entered in hh,min,and sec into seconds

time1=int(input('enter your hour:'))
time2=int(input('enter your minute:'))
time3=int(input('enter your second:'))

# for hour
a=time1*60
b=a*60

# for minute
c=time2*60

# for second
d=time3

# all time into seonds
given_time=b + c + d
print('your time in second is:',given_time)