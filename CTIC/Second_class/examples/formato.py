#!/usr/bin/env python
# -*- coding: utf-8 -*-
monto = eval(input("Ingrese el monto de inversión: "))
years = int(input("Ingrese el número de años: "))
tasa = eval(input("Ingrese la tasa: "))
tasa = tasa / 100
balIni = monto
totalInteres = 0

print(f"{'Año'.rjust(4)} {'Balance inicial'.ljust(16)} {'Interés'.rjust(8)} {'Balance final'.ljust(14)}")
# s.rjust, s.ljust and s.center are available.
for year in range(1, years + 1):
	interes = balIni*tasa
	balFinal = balIni + interes
	print(f"{year:>4} {balIni:<5.2f} {interes:>19.2f} {balFinal:<5.2f}")
	balIni = balFinal
	totalInteres += interes

print(f"Balance final: ${balFinal:8.2f}.")
print(f"Total de Interés ganado: ${balFinal - monto:8.2f}.")