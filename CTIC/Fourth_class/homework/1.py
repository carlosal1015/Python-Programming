#!/usr/bin/env python
# -*- coding: utf-8 -*-
phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dolor sed viverra ipsum nunc aliquet bibendum enim."

list_phrase = phrase.split()

list_phrase.reverse()
phrase = ' '.join(list_phrase)
print(phrase)

'hello world'[::-1]