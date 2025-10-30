# find larger in 3 numbers
a=int(input('enter a:'))
b=int(input('enter b:'))
c=int(input('enter c:'))

if a>b and a>c:
    print(f'{a} is largest')
    
elif b>c:
    print(f'{b} is largest')

else:
    print(f'{c} is largest')
