# Pregunta 13
from tkinter import Tk, Label, mainloop, BOTH, Button, LEFT, RIGHT

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        # Crea widget label
        self.label = Label(self, text = "Choose one", bg = "green1", fg = "purple1")
        # Llama al m'etodo pack para cada widget Label
        self.label.pack(fill = BOTH, expand = 1, padx = 100, pady = 50)
        
        hello_button = Button(self, text = "Say Hello", command = self.say_hello, bg = "white", fg = "brown1") # Llamamos al m'etodo para cambiar la etiqueta
        hello_button.pack(side = LEFT, padx = (20, 0), pady = (0, 20))

        goodbye_button = Button(self, text = "Say Goodbye", command = self.say_goodbye, bg = "yellow1", fg = "blue1")
        goodbye_button.pack(side = RIGHT, padx = (0, 20), pady = (0, 20))


    # Todos los metodos deben de estar alineados para que lo reconozco la clase Window
    def say_hello(self):
        self.label.configure(text = "Hello World!")

    def say_goodbye(self):
        self.label.configure(text = "Goodbye! \n (Closing in 2 seconds)")
        self.after(2000, self.destroy)

# Crea una instancia de la clase MiGUI
if __name__ == "__main__":
    window = Window()
    window.configure(background = "red")
    window.geometry("400x400")
#    label = Label(window, fg = "red")
#    label.pack()
    mainloop()    

# No lleva parentesis en los metodos como argumentos