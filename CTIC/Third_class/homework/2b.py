#!/usr/bin/env python
# -*- coding: utf-8 -*-
def isPrime(number):
	if number == 1:
		print(f"{number} no es primo.")
	i = 2
	while i <= number:
		if number % i == 0:
			print(f"{number} no es primo.")
		else:
			print(f"{number} es primo.")
		break
		i += 1

def main():
	integer = int(input("Ingreso un entero no negativo: "))
	print(isPrime(integer))


if __name__ == "__main__":
	main()