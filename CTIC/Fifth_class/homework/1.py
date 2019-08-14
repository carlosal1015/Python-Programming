#!/usr/bin/env python
# -*- coding: utf-8 -*-
def show(fileName):
	with open(fileName + '.txt', "r+") as f:
		print(f.read())


def delete_string(string, fileName):
	with open(fileName + '.txt', "r+") as f:
		f.readline() # The counter increase by one.
		for line in f:
			if string in line.split():
				print(line.split())
				index = line.split().index(string)
				print(line.split()[index].replace(string, ""))
				line = line.replace(string, "")
				print(line.split())
				#del line.split()[index]


def main():
	#fileName = input("Ingrese el nombre del archivo: ") + '.txt'
	fileName = 'v5alumnos2019'
	#show(fileName)
	#string = input(f"Ingrese el string a eliminar: ")
	string = 'H'
	delete_string(string, fileName)
	#show(fileName)


if __name__ == "__main__":
	main()


"""
a = [2,3,4,5,6,7,8,9,0]
xyz = [0,12,4,6,242,7,9]
print([x for x in xyz if x in a])
"""