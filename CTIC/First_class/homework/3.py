#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script is used to closest point to the first point.

Author: Oromion
Date: 02/08/2019
"""
from math import sqrt, sin, cos, pi
from random import random as rd

RADIUS = 10
x, y = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0] # [0]*4 no funciona!
# x, y son objetos diferentes para que genere valores aleatorios distintos!

for i in range(5):
	theta = 2*pi*rd() # \theta \in [0, 2\pi).
	radius = RADIUS*rd() # r \in \in [0, 10).
	x[i], y[i] = radius*cos(theta), radius*sin(theta)
	print(f"\t{x[i]} \t {y[i]}")

distances = [sqrt((x[0] - x[i+1])**2 + (y[0] - y[i+1])**2) for i in range(4)]
print(distances)

index = distances.index(min(distances))
print(index)
print(f"El punto N°{index+1} es el más cercano al primer punto.")