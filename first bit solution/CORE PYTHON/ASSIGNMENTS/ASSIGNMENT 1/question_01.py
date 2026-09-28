# Write a program to calculate the percentage of student based on marks of any 5 subjects

# TAKE THE MARKS FROM THE USER
english=int(input('enter the marks of english:'))
hindi=int(input('enter the marks of hindi:'))
Mathematics=int(input('enter the marks of Mathematics:'))
science=int(input('enter the marks of science:'))
social_science=int(input('enter the marks of social science:'))

percentage=((english+hindi+Mathematics+science+social_science)/500)*100
print('your overall percentage is:',percentage)