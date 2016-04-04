from decimal import Decimal
import math

x=(3-2)
print ('resultado 1.(i)')
print Decimal(x+2**-54)


x=Decimal(2**-54)
y=Decimal(2-x)
z=Decimal(3)
print ('Resultado 1.(ii)')
print Decimal(z-y)

#----------------------
print ('--------o--------')
x=Decimal(2**-54)
i=Decimal(math.sin(x))
print ('Resultado 2.(i)')
print i
y=Decimal(2**-53)
sin=Decimal(math.sin(y))
cos=Decimal(math.cos(y))
print ('Resultado 2.(ii)')
ii=Decimal(Decimal(2)*sin*cos)
print ii