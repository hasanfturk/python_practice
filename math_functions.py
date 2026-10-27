"""
# round ->en yakın sayıya yuvarlar
x = 2.678
print(round(x))
print(round(x,1))

#abs-> mutlak değer(absolute value)
a = -10
print(abs(a))
"""

"""
import math

#floor() sayıyı kendisine en yakın küçük tam sayıya yuvarlar
print(math.floor(5.6))

#ceil() sayıyı kendisine en yakın büyük tam sayıya yuvarlar
print(math.ceil(1.2))

#sqrt() -> karekök alma
print(math.sqrt(4))

#pow() üs alma
print(math.pow(2,3))

#log -> math.log(x,base)
print(math.log(8,2))
print(math.log(100))    #ln(100)
print(math.log10(1000))
"""

from math import floor,ceil

print(floor(1.2))
print(ceil(1.2))