#!/usr/bin/env python
# -*- coding: utf-8 -*-
def add(line , fileName):
	with open(fileName + '.txt', "a+") as f:
		f.writelines(line)


def main():
	line1 = "\nL74	68 	2	UDP	40	H	22,4600343"
	line2 = "\nL68	63 	1	ALI	37	M	22,3214285"
	#fileName = input("Ingrese el nombre del archivo: ") + '.txt'
	fileName = 'v5alumnos2019'
	add(line1, fileName)
	add(line2, fileName)


if __name__ == "__main__":
	main()