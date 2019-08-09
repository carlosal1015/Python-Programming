=======
Tarea 3
=======

.. code:: python

	string = input("Ingrese una cadena: ")
	i = 0

	while (i < len(string)):
		if string[i] == 'a':
			print(f"'a' encontrado en la posición {i+1}.")
		i +=1

	print("Se imprime la cadena: ", end="")
	for simb in string:
		print(f"{simb}", end="")

	for simb in string:
		print(f"{simb}")

.. code:: python

	from random import random as rd

	celsius2fahrenheit = lambda degrees: (9/5)*degrees + 32

	temperatures = [-273.15*rd() + (1-rd())*99.9839 for i in range(10)]
	#°C
	temps = [("Berlin", 29)]
	c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

	list(map(c_to_f, temps))

	full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
	full_name("   leonhard" , "EULER")

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

.. code:: python