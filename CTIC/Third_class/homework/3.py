#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script is used to create the models for the project app.

Author: Oromion
Date: 05/08/2019
"""
string = input("Ingrese una cadena: ")
i = 0

while (i < len(string)):
	if string[i] == 'a':
		print(f"'a' encontrado en la posición {i+1}.")
	i +=1

print("Se imprime la cadena: ", end="")

# Horizontal
for simb in string:
	print(f"{simb}", end="")

# Vertical
for simb in string:
	print(f"{simb}")