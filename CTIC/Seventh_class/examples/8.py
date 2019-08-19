# Pregunta 14
from tkinter import Tk, Label, mainloop, BOTH, Button, LEFT, RIGHT
from random import randint as rd

class Window(Tk):
	def __init__(self):
		super().__init__()
		self.title("Hello Tkinter")
		self.label_random = Label(self, text = "Generación de números aleatorios", bg = "green1", fg = "purple1")
		self.label_random.pack(fill = BOTH, expand = 1, padx = 100, pady = 50)
		#self.label_random.configure(command = self.print_random)


		self.label_summation = Label(self, text = "Suma de los números aleatorios", bg = "orange1")
		self.label_summation.pack(fill = BOTH, expand = 1, padx = 100, pady = 50)

		self.label_maxmin = Label(self, text = "Máximo y mínimo", bg = "green1", fg = "purple1", font = ("Helvetica", 16))
		self.label_maxmin.pack(fill = BOTH, expand = 1, padx = 100, pady = 50)

		random_numbers = [rd(0, 9) for i in range(10)]

		#random_button = Button(self, text = "Los números aleatorios son", command = self.print_random(random_numbers), bg = "white", fg = "brown1")
		#random_button.pack(side = LEFT, padx = (20, 0), pady = (0, 20))

		#summation_button = Button(self, text = "La suma de la lista", command = self.summation(my_lista), bg = "white", fg = "brown1")
		#summation_button.pack(side = LEFT, padx = (20, 0), pady = (0, 20))

		#maxmin_button = Button(self, text = "El máximo y mínimo es", command = self.maxmin(my_list), bg = "white", fg = "brown1")
		#maxmin_button.pack(side = LEFT, padx = (20, 0), pady = (0, 20))


	def print_random(self, my_lista):
		newlist = []
		for i in range(len(my_lista)):
			newlist[i] = my_lista[i]
		self.label_random.configure(text = ' '.join(my_lista))


	def summation(self, my_list):
		self.label_summation.configure(text = str(sum(my_list)))


	def maxmin(self, my_list):
		max_my_list, min_my_list = max(my_list), min(my_list)
		self.label_summation.configure(text = "El máximo es " + str(max_my_list) + "y el mínimo es " + str(min_my_list))


if __name__ == "__main__":
	window = Window()
	window.configure(background = "red")
	window.geometry("400x400")
	mainloop()


"""
Cola, árbol y pila.
pygubu-designer
tkinter python interface to tcl/tk
tkdocs
"""