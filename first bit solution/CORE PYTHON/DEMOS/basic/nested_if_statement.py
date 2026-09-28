# check weather the boy or girl is eligible for marrage or not 

gender=str(input('enter the gender of the person (male/female):'))
age=int(input('enter the age of the person:'))
if(gender=='male'):
    if(age>=22):
        print('the BOY is eligible for marriage:')
    else:
        print('the BOY is not eligible for marriage:')
else:
    if(age>=18):
        print('the GIRL is eligible for marriage:')
    else:
        print('the GIRL is not eligible for marriage:')
