from math import gcd

class Fraccion(object):
	"""Resumen de la clase Fraccion:
	>>> my_fraction = Fraccion(1, 2)
	"""
	def __init__(self, numerator, denominator):
		self._num = numerator
		self._den = denominator


	def __add__(self, other):
		assert type(other) == Fraccion
		summation_num = self._num*other._den + self._den*other._num
		summation_den = self._den*other._den
		common_divisor = gcd(abs(summation_num), abs(summation_den))
		summation_num //= common_divisor
		summation_den //= common_divisor
		return Fraccion(summation_num, summation_den)


	def __mul__(self, other):
		assert type(other) == Fraccion
		product_num = self._num*other._num
		product_den = self._den*other._den
		common_divisor = gcd(abs(product_num), abs(product_den))
		product_num //= common_divisor
		product_den //= common_divisor
		return Fraccion(product_num, product_den)


	def __eq__(self, other):
		if type(q) != Fraccion:
			return False
		firstNumber = self._num*other._den
		secondNumber = self._den*other._num
		return firstNumber == secondNumber


	def __lt__(self, other):
		firstNumber = self._num*other._den
		secondNumber = self._den*other._num
		return firstNumber < secondNumber


	def sumar(self, other):
		return Fraccion(self._num, self._den).__add__(Fraccion(other._num, other._den))

	def multiplicar(self, other):
		return Fraccion(self._num, self._den).__mul__(Fraccion(other._num, other._den))

	def __str__(self):
		if self._num*self._den >= 0:
			return f"$\\frac{{{abs(self._num)}}}{{{abs(self._den)}}}$"
		else:
			return f"$-\\frac{{{abs(self._num)}}}{{{abs(self._den)}}}$"