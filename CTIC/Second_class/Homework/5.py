#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script is used to create the models for the project app.

Author: Oromion
Date: 02/08/2019
"""
tempo_test = [float(input(f"Ingrese el tiempo de la prueba N°{i+1}: ")) for i in range(10)]
mean = sum(tempo_test) / float(len(tempo_test))

for j in range(10):
    if tempo_test[j] > 16:
        condition = False
        break
    else: condition = True

if (max(tempo_test) <= 16 or condition or mean <= 15):
    print("Apto para la prueba.")
else:
    print("No apto para la prueba.")