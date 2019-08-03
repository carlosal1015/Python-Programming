# Definición de la función
def producto(number_1, number_2):
    """Imprime el producto de dos números"""
    y = number_1*number_2
    return y


##############################################################
# Programa principal
n1 = float(input("Ingresa el número 1: "))
n2 = float(input("Ingresa el número 2: "))

# Invocación de la función
z = producto(n1, n2)

print(z)

# TODO: Pasar la idea de referencia de punteros a Guadalupe
"""
El acceso a las variables es solo en la función principal
"""