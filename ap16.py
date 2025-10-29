#print ()with formatted () function
ht=5
ba=3
areat=0.5*ht*ba
#index place holder
#chaning the dat align can be done by <-left,>-right,^-center. 
print('ht={:<20} ba={:<20} area of triangle={:<20}'.format(ht,ba,areat))
print('ht={:>20} ba={:>20} area of triangle={:>20}'.format(ht,ba,areat))
print('ht={:^20} ba={:^20} area of triangle={:^20}'.format(ht,ba,areat))