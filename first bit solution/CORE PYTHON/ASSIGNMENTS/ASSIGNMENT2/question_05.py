# WAP to calculate selling price of book based on cost price and discount

original_amount=float(input('enter the value of the book:'))
given_discount=float(input('enter the discount given:'))

a=(original_amount*given_discount)
b=(a/100)
c=original_amount-b

print('your price according to your original price and given discount is:',c)