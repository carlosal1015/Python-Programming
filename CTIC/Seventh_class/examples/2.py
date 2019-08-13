from tkinter import Tk, Label, mainloop

class MiGUI(object):
    def __init__(self):
        # Crea el widget ventana
        self.ventana = Tk()
        # Crea el widget label
        self.label = Label(self.ventana, text = "Hola mundo!")
        # Llama el metodo pack del widget Label
        self.label.pack()
        mainloop()

mi_gui = MiGUI()