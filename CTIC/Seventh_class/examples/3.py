from tkinter import Tk, Button, mainloop

class MiGUI:
    def __init__(self):
        ventana = Tk()
        ventana.geometry("400x400")
        self.boton = Button(ventana, text = "Salir", command = ventana.destroy)
        self.boton.pack()
        mainloop()

mi_gui = MiGUI()