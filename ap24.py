# find larger in 3 numbers
a=int(input('enter a:'))
b=int(input('enter b:'))
c=int(input('enter c:'))
d=int(input('enter d:'))
e=int(input('enter c:'))


if a>b and a>c and a>d and a>e:
    print(f'{a} is largest')
    
elif b>c and b>d and b>e:
    print(f'{b} is largest')
    
elif c>d and c>e:
    print(f'{c} is largest')
    
elif d>e:
    print(f'{d} is largest')

else:
    print(f'{e} is largest')