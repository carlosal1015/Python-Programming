from tkinter import Tk, Label, mainloop

class MiGUI(object):
	def __init__(self):
		"""Crea el widget ventana, label y usa el método pack."""
		self.ventana = Tk()
		self.label = Label(self.ventana, text = "Hola mundo!")
		self.label.pack()
		mainloop()

mi_gui = MiGUI()