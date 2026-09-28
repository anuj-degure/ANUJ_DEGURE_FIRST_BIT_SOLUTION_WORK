num=int(input('enter your number:'))

if(num>0):
    for i in range(2,num//2+1):
        if(num % i == 0):
           print(f'{num} is not a prime number.')
        break
    else:
        print(f'{num} is a prime number.')
else:
    print(f'{num} is a not a prime number')
    



