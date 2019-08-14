#!/usr/bin/env python
# -*- coding: utf-8 -*-
phrase = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Dolor sed viverra ipsum nunc aliquet bibendum enim"""
#phrase = input("Por favor ingrese un texto no vacío: ")
list_phrase = phrase.split()

print("Se va a remover la letra central si tiene tamaño impar:")

for i in range(len(list_phrase)):
	if len(list_phrase[i]) % 2 == 1:
		list_phrase[i] = list_phrase[i][:len(list_phrase[i])//2] + list_phrase[i][len(list_phrase[i])//2+1:]

print(' '.join(list_phrase))