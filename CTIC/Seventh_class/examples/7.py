# Pregunta 13
from tkinter import Tk, Label, mainloop, BOTH, Button, LEFT, RIGHT

class Window(Tk):
	def __init__(self):
		super().__init__()
		self.title("Hello Tkinter")
		self.label = Label(self, text = "Choose one", bg = "green1", fg = "purple1")
		self.label.pack(fill = BOTH, expand = 1, padx = 100, pady = 50)
		hello_button = Button(self, text = "Say Hello", command = self.say_hello, bg = "white", fg = "brown1")
		hello_button.pack(side = LEFT, padx = (20, 0), pady = (0, 20))
		goodbye_button = Button(self, text = "Say Goodbye", command = self.say_goodbye, bg = "yellow1", fg = "blue1")
		goodbye_button.pack(side = RIGHT, padx = (0, 20), pady = (0, 20))


	def say_hello(self):
		self.label.configure(text = "Hello World!")


	def say_goodbye(self):
		self.label.configure(text = "Goodbye! \n (Closing in 2 seconds)")
		self.after(2000, self.destroy)


if __name__ == "__main__":
	window = Window()
	window.configure(background = "red")
	window.geometry("400x400")
#    label = Label(window, fg = "red")
#    label.pack()
	mainloop()    
# No lleva parentesis en los metodos como argumentos