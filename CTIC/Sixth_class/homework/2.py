#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
	empleados_dictionary = {
			1000:dict(Nombre = "Juan", Fecha_ingreso = '10-10-17', Department = 103),
			1001:dict(Nombre = "María", Fecha_ingreso = '12-11-13', Department = 104),
			1002:dict(Nombre = "Marco", Fecha_ingreso = '09-07-15', Department = 103)
		}

	for key, value in empleados_dictionary.items():
		print(f"Persona ID: {key}", end = "\n")
		for k, v in value.items():
			print(f"{k} {v}.", end = "\n")

if __name__ == "__main__":
    main()