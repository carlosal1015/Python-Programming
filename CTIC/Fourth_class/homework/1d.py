#!/usr/bin/env python
# -*- coding: utf-8 -*-
phrase = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Dolor sed viverra ipsum nunc aliquet bibendum enim"""
#phrase = input("Por favor ingrese un texto no vacío: ")
non_duplicates = []

print("Se van a imprimir las palabras con una ocurrencia.")

for item in phrase.split():
    if item not in set():
        set().add(item)
        non_duplicates.append(item)

print(' '.join(non_duplicates))