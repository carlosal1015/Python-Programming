from tkinter import Tk, Label, mainloop, BOTH

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        label = Label(self, text = "Hello World!").pack(fill = BOTH, expand = 1, padx = 100, pady = 50)

if __name__ == "__main__":
    window = Window()
    mainloop()