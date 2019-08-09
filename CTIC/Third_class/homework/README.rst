=======
Tarea 3
=======

1. Defina una función que reciba un valor en grados Centígrados y devuelva su valor correspondiente en grados Fahrenheit,

.. math::

	F = \frac{9}{5}C + 32.

Use esta función para escribir un programa que imprima el equivalente de las temperaturas de 0C-100C en forma tabular.

.. code:: python

	from random import random as rd

	celsius2fahrenheit = lambda degrees: (9/5)*degrees + 32
	temperatures_random = [0*rd() + (1-rd())*100 for i in range(100)]

	print(f"{'Número (N)'.rjust(10)} {'Grados Celsius (°C)'.ljust(15)} {'Grados Fahrenheit (°F)'.rjust(15)}")
	for i in range(len(temperatures_random)):
		print(f"{i + 1:>10} {temperatures_random[i]:<5.2f} {celsius2fahrenheit(temperatures_random[i]):>36.2f}")

2. Implemente una función que determine si un número ingresado del teclado es primo. Escriba un programa para probar la función.

a) la función debe devolver algún valor que indiqe que el número es o no es primo.

.. code:: python

	def isPrime(n):
		if n ==1:
			return False
		i = 2
		while i**2 <= n:
			if n % i == 0:
				return False
			i += 1
		return True

	number = int(input("Ingreso un enterno no negativo: "))

	if isPrime(number):
		print(f"{number} es primo.")
	else:
		print(f"{number} no es primo.")

b) la función no devuelve ningún valor, indica si es o no es primo directamente en pantalla.

.. code:: python

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


3. Ingresar un string del teclado y determinar si la letra `a` se encuentra en él y la posición donde se encuentra.
Imprimir también los elementos del string.

.. code:: python

	string = input("Ingrese una cadena: ")
	i = 0

	while (i < len(string)):
		if string[i] == 'a':
			print(f"'a' encontrado en la posición {i+1}.")
		i +=1

	print("Se imprime la cadena: ", end="")

	# Horizontal
	for simb in string:
		print(f"{simb}", end="")