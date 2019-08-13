from tkinter import Tk, Label, mainloop, BOTH, Button, LEFT, RIGHT

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        # Crea widget label
        self.label = Label(self, text = "Choose one")
        # Llama al m'etodo pack para cada widget Label
        self.label.pack(fill = BOTH, expand = 1, padx = 100, pady = 50)
        
        hello_button = Button(self, text = "Say Hello")
        hello_button.pack(side = LEFT, padx = (20, 0), pady = (0, 20))

        goodbye_button = Button(self, text = "Say Goodbye")
        goodbye_button.pack(side = RIGHT, padx = (0, 20), pady = (0, 20))

# Crea una instancia de la clase MiGUI
if __name__ == "__main__":
    window = Window()
    mainloop()