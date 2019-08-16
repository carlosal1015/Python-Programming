from math import gcd

class Fraccion(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    
    def sumar(self, other):
        summation_numerator = self.numerator*other.denominator + self.denominator*other.numerator
        summation_denominator = self.denominator*other.denominator
        common_divisor = gcd(abs(summation_numerator), abs(summation_denominator))
        summation_numerator //= common_divisor
        summation_denominator //= common_divisor

        return Fraccion(summation_numerator, summation_denominator)

    def multiplicar(self, other):
        product_numerator = self.numerator*other.numerator
        product_denominator = self.denominator*other.denominator
        common_divisor = gcd(abs(product_numerator), abs(product_denominator))
        product_numerator //= common_divisor
        product_denominator //= common_divisor

        return Fraccion(product_numerator, product_denominator)


    def __pos__(self, other):
        pass

    
    def __mul__(self, other):
        pass

    
    def __eq__(self, other):
        firstNumber = self.numerator*other.denominator
        secondNumber = self.denominator*other.numerator

        return firstNumber == secondNumber

    def __lt__(self, other):
        pass


    def __str__(self):
        return f"$\\frac{{{self.numerator}}}{{{self.denominator}}}$"