#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hola
"""
from random import random as rd

celsius2fahrenheit = lambda degrees: (9/5)*degrees + 32

temperatures = [-273.15*rd() + (1-rd())*99.9839 for i in range(10)]
#°C
temps = [("Berlin", 29)]
c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

list(map(c_to_f, temps))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
full_name("   leonhard" , "EULER")