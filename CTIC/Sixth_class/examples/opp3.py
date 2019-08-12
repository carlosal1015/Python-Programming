"""
Se recomienda que los valores inicializados sean con el constructor __init__
"""
# Ejemplo de diseño de una clase básica

# Diseño de la clase
class Punto:
    x = 0
    y = 0
# Test (Prueba de la clase)
# Creación de los objetos
p1 = Punto() # Instanciando una clase
print(f"P_1 = ({p1.x},{p1.y})")

p1.x = 3
p1.y = 5

print(f"P_1 = ({p1.x},{p1.y})")