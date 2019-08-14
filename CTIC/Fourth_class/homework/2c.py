#!/usr/bin/env python
# -*- coding: utf-8 -*-
phrase = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Dolor sed viverra ipsum nunc aliquet bibendum enim"""
#phrase = input("Por favor ingrese un texto no vacío: ")
list_phrase = phrase.split()
length = [ len(list_phrase[i]) for i in range(len(list_phrase)) ]
list_of_tuples = list(zip(length, list_phrase))
list_of_tuples.sort()