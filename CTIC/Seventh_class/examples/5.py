from tkinter import Tk, Label, mainloop, BOTH, Button, LEFT, RIGHT

class Window(Tk):
	"""Hereda la ventana Tk, crea el widget label y llama al método pack para cada widget Label."""
	def __init__(self):
		super().__init__()
		self.title("Hello Tkinter")
		self.label = Label(self, text = "Choose one")
		self.label.pack(fill = BOTH, expand = 1, padx = 100, pady = 50)
		hello_button = Button(self, text = "Say Hello")
		hello_button.pack(side = LEFT, padx = (20, 0), pady = (0, 20))
		goodbye_button = Button(self, text = "Say Goodbye")
		goodbye_button.pack(side = RIGHT, padx = (0, 20), pady = (0, 20))


if __name__ == "__main__":
	window = Window()
	mainloop()