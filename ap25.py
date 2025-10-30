# simple math calculator
a=int(input('enter a number :'))
op=input('enter operator (+,-,*,/) :')
b = int(input('enter a number ='))

if op == '+':
    res = a+b
    print('result = {}'.format(res))
    
     
elif op == '-':
    res = a-b
    print('result = {}'.format(res))
    
  
elif op == '*':
    res = a*b
    print('result = {}'.format(res))
    
   
elif op == '/':
    res = a/b
    print('result = {}'.format(res))
    
else:
    print(" Not a math opertor")
    