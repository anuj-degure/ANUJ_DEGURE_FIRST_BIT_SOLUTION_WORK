# convert distant given in feet and inches into meter and centimeter

feet=float(input('enter the value in feet:'))
inch=float(input('enter the value in inch:'))
a=feet*0.3048 #feet to meter conversion
b=inch*2.54 #inch to centimeter conversion

print('your given feet in meter is:',a)
print('your given inch in centimeter is:',b)