#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
	employees = {
		1000:{'Nombre': "Juan", 'Fecha': '10-10-17', 'Department': 103},
		1001:{'Nombre': "Mary", 'Fecha': '01-11-88', 'Department': 101},
		1002:{'Nombre': "Roberto", 'Fecha': '11-02-19', 'Department': 105},
		1003:{'Nombre': "Lizbeth", 'Fecha': '22-06-11', 'Department': 104},
	}
	print(f"Diccionario de empleados ordenado descendentemente con respecto a sus nombres.")
	print(sorted(employees.items(), key = lambda x: x[1]['Nombre'], reverse = True))


if __name__ == "__main__":
	main()