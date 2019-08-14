#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Aquellas palabras que sean mayores que la anterior y menores que la posterior alfabéticamente.
"""
phrase = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Dolor sed viverra ipsum nunc aliquet bibendum enim"""
#phrase = input("Por favor ingrese un texto no vacío: ")

list_phrase = phrase.split()

print("Se imprime las palabras que sean mayores que la anterior\
y menos que la posterior alfabéticamente:")

for i in range(len(list_phrase)-2):
    if list_phrase[i] < list_phrase[i+1] < list_phrase[i+2]:
        print(list_phrase[i+1])