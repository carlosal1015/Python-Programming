#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script is used to create the models for the project app.

Author: Oromion
Date: 02/08/2019
"""
from money import Money

factory = Money(amount = eval(input("Ingrese el saldo de la empresa:")), currency = 'USD')
computo = Money(5000, 'USD')
mobiliario = Money(2000, 'USD')

if factory.amount < 0:
    loan = Money(10000, 'USD') - factory
    factory = Money(10000, 'USD')
elif factory.amount <= 20000:
    loan = Money(20000, 'USD') - factory
    factory = Money(20000, 'USD')

resto = factory - (computo + mobiliario)
insumos = incentivos = Money(amount = resto.amount/2, currency = 'USD')

print(f"Se destinará {insumos.amount} {insumos.currency} para la compra de insumos.")
print(f"Se destinará {incentivos.amount} {incentivos.currency} para los incentivos del personal.")
print(f"Pedirá un préstamo de {loan.amount} {loan.currency}.")