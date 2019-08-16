from math import gcd

class Fraccion(object):
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator / gcd(abs(numerator), abs(denominator)))
        self.denominator = int(denominator / gcd(abs(numerator), abs(denominator)))

    
    def sumar(self, other):
        summation_numerator = self.numerator*other.denominator + self.denominator*other.numerator
        summation_denominator = self.denominator*other.denominator
        return f"$\\frac{{{summation_numerator}}}{{{summation_denominator}}}$"


    def multiplicar(self, other):
        product_numerator = self.numerator*other.numerator
        product_denominator = self.denominator*other.denominator
        return f"$\\frac{{{product_numerator}}}{{{product_denominator}}}$"


    def __pos__(self, other):
        pass

    
    def __mul__(self, other):
        pass

    
    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass


    def __str__(self):
        return f"$\\frac{{{self.numerator}}}{{{self.denominator}}}$"