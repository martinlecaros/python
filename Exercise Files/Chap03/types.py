#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 'prueba "{1:<03}" "{0:>09}"'.format(8,5)
print('x is {}'.format(x))
print(type(x))

z = 5 // 3
print (z)

from decimal import *
a = Decimal('.10')
b = Decimal('.30')

n = a + a + a - b
print(f'Resultado: {n}')
print(type(n))