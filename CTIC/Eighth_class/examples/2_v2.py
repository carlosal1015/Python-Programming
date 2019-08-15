from tkinter import Tk, Label, mainloop, Frame, Entry, Button, StringVar

class Mi_GUI():
    def __init__(self):
        self.window = Tk()
        self.frame_sup = Frame(self.window)
        self.frame_medio = Frame(self.window)
        self.frame_inf = Frame(self.window)

        self.label_distance = Label(self.frame_sup, text = "Ingrese una distancia en km: ")
        self.entry = Entry(self.frame_sup, width = 10)
        self.label_distance.pack(side = 'left')
        self.entry.pack(side = 'left')

        self.label_description = Label(self.frame_medio, text = "Convertida a millas: ")
        self.valor = StringVar()
        self.label_millas = Label(self.frame_medio, textvariable = self.valor)

        # Posicionando las etiquetas
        self.label_description.pack(side = "left")
        self.label_millas.pack(side = "left")

        self.button_converter = Button(self.frame_inf, text = "Convertir", command = self.convertir)
        self.button_exit = Button(self.frame_inf, text = "Salir", command = self.window.destroy)
        
        # Posicionamiento de los botones

        self.button_converter.pack(side = 'left')
        self.button_exit.pack(side = 'left')

        self.frame_sup.pack()
        self.frame_medio.pack()
        self.frame_inf.pack()

        # Inicia el mainloop
        mainloop()
    
    def convertir(self):
        while True:
            try:
                kilo = float(self.entry.get())
                millas = kilo*0.6214
                # Convierte kilo a millas y lo asigna en el objeto StringVar
                # Este automáticamanete actualizará el widget label_millas
                self.valor.set(millas)
                break
            except ValueError:
                self.valor.set("Debe ingresar un número!")

my_gui = Mi_GUI()