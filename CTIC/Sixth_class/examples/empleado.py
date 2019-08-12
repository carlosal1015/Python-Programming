class Empleado:
    def __init__(self):
        self.codigo = input(f"Ingrese un código: ")
        self.nombre = input(f"Ingrese un nombre: ")
    
    def visualizar(self):
        print(f"Su código es {self.codigo} y su nombre es {self.nombre}.")