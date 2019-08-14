#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
El ítem a consiste en imprimir la misma secuencia,
pero en orden contrario.
"""
phrase = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Dolor sed viverra ipsum nunc aliquet bibendum enim"""
#phrase = input("Por favor ingrese un texto no vacío: ")

list_phrase = phrase.split()
list_phrase.reverse()
print(f"En orden contrario: {' '.join(list_phrase)}.")
#'hello world'[::-1]