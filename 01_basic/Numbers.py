x=2
y=3
z=4
print((x+y)*z)
## print("Manish"+z) typeError
print('Manish'+'Raaz')
print(x,y,z)
print(2**10)

# print(5/0) ZeroDivisionError
print(0/10)

# print(repr('Manish')) Ye object ka official/debug representation return karta hai.
# print(str('Manish')) Strings me quotes remove ho jate hain.
print(('Manish'))


# print('manish'<'Aaaz') false because of ASCII

print(4!=5)
print(x<y<z)

import math
# print(math.floor(-4.5)) closet value to bottom
print(math.factorial(5))
# print(math.trunc(4.6)) towards nearest zero

print((4+4j)*3)
print((4+2j)**2)
print(15*16+15)

# print(0o30) octal
# print(0X30) hexa
# print(0b48) binary

print(oct(48))
print(hex(98))

print(x<<4)

import random
print(random.random())
print(random.randint(1,100))

number=[10,20,30,40,50,60]
print(random.choice(number))


print(0.1+0.1+0.1)
print((0.1+0.1+0.1)-0.3)

from decimal import Decimal
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))


