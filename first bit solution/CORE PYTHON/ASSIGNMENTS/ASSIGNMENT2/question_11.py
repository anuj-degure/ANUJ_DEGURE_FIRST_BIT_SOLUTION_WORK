# Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.

amount=int(input('enter the amount of your money:'))
a=amount//500
b=(amount%500)//200
c=((amount%500)%200)//100
d=(((amount%500)%200)%100)//50
e=((((amount%500)%200)%100)%50)//20
f=(((((amount%500)%200)%100)%50)%20)//10

print('For your amount you need',a,'notes of 500rs')
print('For your amount you need',b,'notes of 200rs')
print('For your amount you need',c,'notes of 100rs')
print('For your amount you need',d,'notes of 50rs')
print('For your amount you need',e,'notes of 20rs')
print('For your amount you need',f,'notes of 10rs')

# a=110%20
# print(a)