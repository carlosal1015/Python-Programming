#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Empleado(object):
	"""
	>>> peruvian_employee = Empleado()
	>>> japanese_employee = Empleado()
	"""
	counter = 0
	def __init__(self):
		self.id_number = input(f"Ingrese el id: ")
		self.name = input(f"Ingrese el nombre: ")
		self.genre = input(f"Ingrese el género: ")
		self.city = input(f"Ingrese la ciudad: ")
		self.salary = eval(input(f"Ingrese el salario: "))
		Empleado.counter += 1


	def show(self):
		return (f"El código es {self.id_number}.\n"
		f"Su nombre es {self.name}.\n"
		f"Su género es {self.genre}.\n"
		f"La ciudad es {self.city}.\n"
		f"El salario es S/{self.salary}."
		)


	def update(self):
		self.id_number = input(f"Modificar el id: ")
		self.name = input(f"Modificar el nombre: ")
		self.genre = input(f"Modificar el género: ")
		self.city = input(f"Modificar la ciudad: ")
		self.salary = eval(input(f"Modificar el salario: "))


peruvian_employee = Empleado()
#('PER23', 'Raúl', 'M', 'Trujillo', 2000)
print(Empleado.counter)
print(peruvian_employee.show())
print(peruvian_employee.update())
print(peruvian_employee.show())
#japanese_employee = Empleado()
# #('JAP14', 'Momo', 'F', 'Osaka', 3200)