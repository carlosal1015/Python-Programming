#!/usr/bin/env python
# -*- coding: utf-8 -*-
def isPrime(number):
	"""
	Programa que determina la primalidad de un número natural.
	"""
	value = False
	if number == 1 :
		value = False
	elif number == 2:
		value = True
	elif number == 3:
		value = True
	i = 2
	while i**2 <= number:
		if number % i == 0:
			value = False
			break
		value = True
		i += 1

	if value:
		print(f"{number} es un número primo.")
	else:
		print(f"{number} no es un número primo.")

#def main():
integer = int(input("Ingrese un entero no negativo: "))
print(isPrime(integer))

#if __name__ == "__main__":
#	main()