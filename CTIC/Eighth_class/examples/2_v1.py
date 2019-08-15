from tkinter import Tk, Label, mainloop, Frame, Entry, Button

class Mi_GUI():
    def __init__(self):
        self.window = Tk()
        self.frame_sup = Frame(self.window)
        self.frame_inf = Frame(self.window)

        self.label_message = Label(self.window,\
            text = "Ingrese una distancia en km: ")

        self.entry = Entry(self.frame_sup, width = 10)
        self.label_message.pack(side = 'left')
        self.entry.pack(side = 'left')

        self.button_converter = Button(self.frame_inf, text = "Convertir", command = self.convertir)
        self.button_exit = Button(self.frame_inf, text = "Salir", command = self.window.destroy)
        
        # Posicionamiento de los botones

        self.button_converter.pack(side = 'left')
        self.button_exit.pack(side = 'left')

        self.frame_sup.pack()
        self.frame_inf.pack()


        # Inicia el mainloop
        mainloop()
    
    def convertir(self):
        kilo = float(self.entry.get())
        millas = kilo*0.6214

        # Convierte kilo a millas y lo muestra  en el intérprete
        print(millas)

my_gui = Mi_GUI()