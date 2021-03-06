from tkinter import Tk, Button, mainloop, Frame

class Application(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side = "top")

        self.quit = Button(self, text = "QUIT", fg = "red", command = self.master.destroy)

        self.quit.pack(side = "bottom")

        mainloop()

    def say_hi(self):
        print("hi there, everyone!")



root = Tk()
app = Application(master = root)