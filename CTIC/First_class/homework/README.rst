=======
Tarea 1
=======

1. Escriba un programa que pida al usuario ingresar una hora (expresada en horas y minutos
usando un reloj de 24 horas). El programa luego muestra las horas de salida y llegada para
el vuelo cuyo tiempo de partida es más cercano al ingresado por el usuario:

Ingrese la hora en formato de 24 horas: 13:15
Tiempo de partida más cercano es 12:47 p.m., llegada a las 3:19 p.m.

.. code:: python

	from datetime import datetime as dt

	hora_salida = ['08:00' ,'09:43', '11:19', '12:47', '14:00', '15:45', '19:00', '21:45']
	hora_llegada = ['10:16', '11:52', '13:31', '15:19', '16:08', '17:55', '21:20', '23:58']

	print("Ingrese la hora en formato de 24 horas:")

	hora_consultada = input("Hora: ")
	minuto_consultado = input("Minutos: ")

	consulta = dt.strptime(hora_consultada + ":" + minuto_consultado, "%H:%M")
	hora_cercana = min(hora_salida, key=lambda t: abs(dt.strptime(t, "%H:%M") - consulta))

	index = hora_salida.index(hora_cercana)
	print(f"Tiempo de partida más cercano es {hora_cercana}, llegada a las {hora_llegada[index]}")

2. El dueño de una empresa desea planificar las decisiones financieras que tomará en el
siguiente año. La manera de planificarlas depende de lo siguiente:

Si actualmente su capital se encuentra con saldo negativo, pedirá un préstamo bancario para
que su nuevo saldo sea de ​$10,000​. Si su capital tiene actualmente un saldo positivo pedirá
un préstamo bancario para tener un nuevo saldo de ​$20,000​, pero si su capital tiene
actualmente un saldo superior a los ​$20,000​ no pedirá ningún préstamo.

Si actualmente su capital se encuentra con saldo negativo, pedirá un préstamo bancario para que
su nuevo saldo sea de​ $10,000​. Si su capital tiene actualmente un saldo positivo pedirá un
préstamo bancario para tener un nuevo saldo de​ $20,000​, pero si su capital tiene actualmente
un saldo superior a los ​$20,000​ no pedirá ningún préstamo.

.. code:: python

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

3. Diseña un programa que, dados cinco puntos en el plano cartesiano con sus coordenadas X,Y;
determine cuál de los cuatro últimos puntos es más cercano al primero.

.. code:: python

	from math import sqrt, sin, cos, pi
	from random import random as rd

	RADIUS = 10
	x, y = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0] # [0]*4 no funciona!
	# x, y son objetos diferentes para que genere valores aleatorios distintos!

	for i in range(5):
		theta = 2*pi*rd() # \theta \in [0, 2\pi).
		radius = RADIUS*rd() # r \in \in [0, 10).
		x[i], y[i] = radius*cos(theta), radius*sin(theta)
		print(f"\t{x[i]} \t {y[i]}")

	distances = [sqrt((x[0] - x[i+1])**2 + (y[0] - y[i+1])**2) for i in range(4)]
	print(distances)

	index = distances.index(min(distances))
	print(index)
	print(f"El punto N°{index+1} es el más cercano al primer punto.")