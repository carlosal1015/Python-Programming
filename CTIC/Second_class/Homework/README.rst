=======
Tarea 2
=======

1. Elaborar un algoritmo que calcule y muestre la suma de todos los mú;tiplos
de cinco comprendidos entre dos valores A y B (ambos inclusive). El programa
no permitirá introducir valores negativos para A y B y verificará que A es
memnor que B. Si A es mayor que B, intercambiará sus valores.

Resuelva el ejercicio paso a paso siguiendo las indicaciones:

a) Asuma que los valores ingresados A y B son correctos y que A<B. Elabore
el bucle (usando `while`) que determine la suma de todos los múltiplos de
cinco.

.. code:: python

	A, B = int(input("Valor de A: ")), int(input("Valor de B: "))

	summation = 0
	n = A

	while n <= B:
		if n % 5 == 0:
			summation += n
		n +=1

	print(f"La suma de todos los múltiplos de 5 entre {A} y {B} es {summation}.")

b) Agregue el código que permita mostrar, en forma horizontal, todos los
números entre A y B.

.. code:: python

	A, B = int(input("Valor de A: ")), int(input("Valor de B: "))

	summation = 0
	n = A

	while n <= B:
		if n % 5 == 0:
			summation += n
		n +=1
		print(n)

	print(f"La suma de todos los múltiplos de 5 entre {A} y {B} es {summation}.")

c) Agregue el código que permita validar los valores de A y B. Si el
usuario ingresa un valor negativo para A, el programa debe imprimir
`Error` y volver a solicitar que ingrese un nuevo valor. Proceder de
la misma manera para B.

.. code:: python

	A, B = int(input("Valor de A: ")), int(input("Valor de B: "))

	while A < 0:
		print("A no pueden ser negativo.")
		A = int(input("Valor de A: "))

	while B < 0:
		print("B no puede ser negativo.")
		B = int(input("Valor de B: "))

	summation = 0
	n = A

	while n <= B:
		if n % 5 == 0:
			summation += n
		n +=1

	print(f"La suma de todos los múltiplos de 5 entre {A} y {B} es {summation}.")

d) Agregue el código que asegure que A<B (si es necesario intercambiar
los valores).

.. code:: python

	A, B = int(input("Valor de A: ")), int(input("Valor de B: "))

	while A < 0:
		print("A no pueden ser negativo.")
		A = int(input("Valor de A: "))

	while B < 0:
		print("B no puede ser negativo.")
		B = int(input("Valor de B: "))

	if B < A:
		A, B = B, A

	summation = 0
	n = A

	while n <= B:
		if n % 5 == 0:
			summation += n
		n +=1

	print(f"La suma de todos los múltiplos de 5 entre {A} y {B} es {summation}.")

e) Elabore una versión nueva edel programa usando `for` (modifique solo
el bucle que determina la suma).

.. code:: python

	A, B = int(input("Valor de A: ")), int(input("Valor de B: "))

	while A < 0:
		print("A no pueden ser negativo.")
		A = int(input("Valor de A: "))

	while B < 0:
		print("B no puede ser negativo.")
		B = int(input("Valor de B: "))

	if B < A:
		A, B = B, A

	summation = 0

	for n in range(A, B + 1):
		if n % 5 == 0:
			summation += n
		n += 1

	print(f"La suma de todos los múltiplos de 5 entre {A} y {B} es {summation}.")

f) Elabore una versión nueva del programa, (usando `while`o `for`) que
permita mostrar todos los números entre A y B en forma vertical y que
para cada valor **múltiplo de cinco** coloque un asterisco a su lado
derecho.

========
Ejemplo:
========

.. code:: bash

	Ingrese el límite inferior: 3
	Ingrese el límite superior: 10
	Los números son:
	3
	4
	5*
	6
	7
	8
	9
	10*
	La suma de los múltiplos de 5 comprendidos entre 3 y 10 es: 15

.. code:: python

	A, B = int(input("Valor de A: ")), int(input("Valor de B: "))

	while A < 0:
		print("A no pueden ser negativo.")
		A = int(input("Valor de A: "))

	while B < 0:
		print("B no puede ser negativo.")
		B = int(input("Valor de B: "))

	if B < A:
		A, B = B, A

	summation = 0

	print("Los números son:")

	for n in range(A, B + 1):
		if n % 5 == 0:
			summation += n
			print(f"{n}*")
		else:
			print(n)
		n += 1

	print(f"La suma de todos los múltiplos de 5 entre {A} y {B} es {summation}.")

2. Un entrenador le ha propuesto a un atleta  recorrer una ruta de cinco
kilómetros durante diez días (un recorrido cada día), para determinar si
es apto para la prueba de cinco kilómetros o debe buscar otra especialidad
deportiva. Para considerarlo apto debe cumplir por lo menos una de las
siguientes condiciones:

- Que en ninguna de las pruebas haga un tiempo mayor a 16 minutos.
- Que solo en una de las pruebas realice un tiempo mayor a 16 minutos.
- Que su promedio de tiempos sea menor o igual a 15 minutos.

.. code:: python

	from statistics import mean

	tempo_test = [float(input(f"Ingrese el tiempo de la prueba N°{i+1}: ")) for i in range(10)]

	for j in range(10):
		if tempo_test[j] > 16:
			condition = False
			break
		else: condition = True

	if (max(tempo_test) <= 16 or condition or mean(tempo_test) <= 15):
		print("Apto para la prueba.")
	else:
		print("No apto para la prueba.")

3. Escriba un programa que calcule las raíces cuadradas.

.. code:: python

	from math import sqrt

	TOLERANCE = 1e-6

	def root_square_numeric(number):
		"""
		Calcula la raíz cuadrada de un número numéricamente
		"""
		estimate = 1.0
		while True:
			estimate = (estimate + number/estimate)/2
			difference = abs(number - estimate**2)
			if difference <= TOLERANCE:
				break
		return estimate

	while True:
		try:
			number = eval(input("Ingrese un número: "))
			if number < 0:
				raise ValueError
			break
		except ValueError:
			print("No es posible calcular raíz cuadrada de números negativos! en \mathbb{R}.")

	print(f"Valor estimado del programa: {root_square_numeric(number)}.")
	print(f"Valor estimado de Python: {sqrt(number)}.")