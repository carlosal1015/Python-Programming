#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Elabore un algortimo que calcule y muestre la suma de todos los múltiplos de 5 comprendidos entre dos
valores A y B (ambos inclusive). El programa no permitira introducir valores negativos para A y B
y verificara que A es menor que B/ Si A es mayor que B, intercambiara sus valores.
"""
A, B = int(input("Valor de A: ")), int(input("Valor de B: "))

summation = 0
n = A

while n <= B:
	if n % 5 == 0:
		summation += n
	n +=1

print(f"La suma de todos los múltiplos de 5 entre {A} y {B} es {summation}.")