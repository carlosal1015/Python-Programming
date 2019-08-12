class Articulo:
    def __init__(self, cd, ct, pr):
        self.cod = cd
        self.cant = ct
        self.pre = pr
    def cantidad(self):
        print(f"Cantidad actual {self.cant}")
    

    def precio(self):
        print(f"Precio actual {self.pre}")
    
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