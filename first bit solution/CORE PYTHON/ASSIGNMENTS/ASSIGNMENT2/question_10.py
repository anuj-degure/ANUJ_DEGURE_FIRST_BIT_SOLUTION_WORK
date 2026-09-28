# Write a program to reverse three-digit number.

num=int(input('entrer the 3 digit number:'))
a=num%10  # its bring output last digit
b=(num//10)%10  #its bring the second last number
c=(num//100)  #its bring the 1st number
d=(a*100)+(b*10)+c


print('the reverse of three digit number is:',d)