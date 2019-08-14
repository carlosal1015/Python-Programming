#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def show(fileName):
	with open(fileName + '.txt', "r+") as f:
		return f"{f.read()}"


def delete_string(string, fileName):
	with open(fileName + '.txt', "r+") as f:
		text = f.read()
		f.seek(0)
		#f.readline() # The counter increase by one.
		text = re.sub(string, '', text)
		f.write(text)
		f.truncate()

def main():
	#fileName = input("Ingrese el nombre del archivo: ") + '.txt'
	fileName = 'v2alumnos2019'
	print(show(fileName))
	#string = input(f"Ingrese el string a eliminar: ")
	string = 'M'
	delete_string(string, fileName)
	print()
	print(show(fileName))


if __name__ == "__main__":
	main()