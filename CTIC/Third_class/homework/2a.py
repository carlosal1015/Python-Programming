#!/usr/bin/env python
# -*- coding: utf-8 -*-
def isPrime(number):
	if number == 1:
		return f"{number} no es primo."
	i = 2
	while i**2 <= number:
		if number % i == 0:
			return f"{number} no es primo."
		i += 1
	return f"{number} es primo."


def main():
	integer = int(input("Ingreso un entero no negativo: "))
	print(isPrime(integer))


if __name__ == "__main__":
	main()