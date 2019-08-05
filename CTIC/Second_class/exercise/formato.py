#!/usr/bin/env python
# -*- coding: utf-8 -*-
monto = eval(input("Ingrese el monto de inversion: "))
years = int(input("Ingrese el numero de anos: "))
tasa = eval(input("Ingrese la tasa: "))
tasa = tasa / 100
balIni = monto
totalInteres = 0
print("%4s%18s%10s%16s"%("Ano", "Balance Inicial", "Interes", "Balance Final"))

# Calcular y mostrar los resultados cada ano

for year in range(1, years+1):
    interes = balIni*tasa
    balFinal = balIni + interes
    print("%4d%18.2f%10.2f%16.2f"%\
          (year, balIni, interes, balFinal))
    balIni = balFinal
    totalInteres += interes

print("Balance Final: $%8.2f"%balFinal)
print("Total de Interes ganado: $%8.2f"%(balFinal-monto))