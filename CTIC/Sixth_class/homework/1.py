#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fraccion import Fraccion as fr

un_medio = fr(numerator = 1, denominator = 2)
dos_tercios = fr(numerator = 2, denominator = 3)

print(un_medio.sumar(dos_tercios))
print(dos_tercios.sumar(un_medio))

print(un_medio.multiplicar(dos_tercios))
print(dos_tercios.multiplicar(un_medio))