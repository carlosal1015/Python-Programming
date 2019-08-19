#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fraccion import Fraccion as fr

un_medio = fr(numerator = -1, denominator = 2)
dos_tercios = fr(numerator = 2, denominator = -3)

# Tres sumas equivalentes
print(f"{dos_tercios} + {un_medio} = {un_medio} + {dos_tercios} = {un_medio + dos_tercios} = {un_medio.sumar(dos_tercios)} = {dos_tercios.sumar(un_medio)}.")
# Tres multiplicaciones equivalentes
print(f"{dos_tercios} * {un_medio} = {un_medio} * {dos_tercios} = {un_medio*dos_tercios} = {un_medio.multiplicar(dos_tercios)} = {dos_tercios.multiplicar(un_medio)}.")