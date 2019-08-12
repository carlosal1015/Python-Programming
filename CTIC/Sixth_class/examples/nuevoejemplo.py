class Articulo1:
    def __init__(self, cd, ct, pr):
        self.cod = cd
        self.cant = ct
        self.pre = pr
    def cantidad(self):
        return self.cant

    def precio(self):
        return self.pre
    
    def vender(self, x):
        if x < self.cant:
            self.cant = self.cant - x
        else:
            print("Cantidad insuficiente.")
    
    def comprar(self, x):
        self.cant = self.cant + x
    
    def status(self):
        print(f"Precio actual de {self.cod} es {self.pre}.")
        print(f"Cantidad actual de {self.cod} es {self.cant}.", end="\n")