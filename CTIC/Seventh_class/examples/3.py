from tkinter import Tk, Button, mainloop

class MiGUI:
	def __init__(self):
		ventana = Tk()
		self.boton = Button(ventana.geometry("400x400"), text = 'Salir', command = ventana.destroy).pack()
		mainloop()

mi_gui = MiGUI()