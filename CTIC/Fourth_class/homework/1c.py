#!/usr/bin/env python
# -*- coding: utf-8 -*-
phrase = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Dolor sed viverra ipsum nunc aliquet bibendum enim"""
phrase = input("Por favor ingrese un texto no vacío: ")
#phrase = input("Por favor ingrese un texto no vacío: ")
list_phrase = phrase.split()
without_repetitions = [item for item in list_phrase if list_phrase.count(item) == 1]
print(' '.join(without_repetitions))