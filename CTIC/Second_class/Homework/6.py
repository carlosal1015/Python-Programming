#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script is used to create the models for the project app.

Author: Oromion
Date: 02/08/2019
"""
from math import sqrt

TOLERANCE = 1e-6

def root_square_numeric(number):
    """
    Calcula la raíz cuadrada de un número numéricamente
    """
    estimate = 1.0
    while True:
        estimate = (estimate + number/estimate)/2
        difference = abs(number - estimate**2)
        if difference <= TOLERANCE:
            break
    return estimate

while True:
    try:
        number = eval(input("Ingrese un número: "))
        if number < 0:
            raise ValueError
        break
    except ValueError:
        print("No es posible calcular raíz cuadrada de números negativos! en R")

print(f"Valor estimado del programa: {root_square_numeric(number)}.")
print(f"Valor estimado de Python: {sqrt(number)}.")