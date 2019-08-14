#!/usr/bin/env python
# -*- coding: utf-8 -*-
phrase = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Dolor sed viverra ipsum nunc aliquet bibendum enim"""
#phrase = input("Por favor ingrese un texto no vacío: ")
list_phrase = phrase.split()
last_four = [None]*len(list_phrase)

print("Se va a imprimir las últimas cuatro letras de cada palabra:")

for i in range(len(list_phrase)):
    last_four[i] = list_phrase[i][-4:]

print(' '.join(last_four))