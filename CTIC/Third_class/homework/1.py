#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Program that convert degree Celsius to Fahrenheit.
"""
from random import random as rd

celsius2fahrenheit = lambda degrees: (9/5)*degrees + 32

#temperatures_random = [0*rd() + (1-rd())*100 for i in range(100)]
temperatures_ordered = [i for i in range(0, 100)]

print(f"{'Número (N)'.rjust(10)} {'Grados Celsius (°C)'.ljust(15)} {'Grados Fahrenheit (°F)'.rjust(15)}")
for i in range(len(temperatures_ordered)):
	#print(f"{i + 1:>10} {temperatures_random[i]:<5.2f} {celsius2fahrenheit(temperatures_random[i]):>36.2f}")
	print(f"{i + 1:>10} {temperatures_ordered[i]:<5.2f} {celsius2fahrenheit(temperatures_ordered[i]):>36.2f}")