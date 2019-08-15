# frame_demo.py
#Este es un programa que crea labels en dos marrcos diferentes
import tkinter

class MiGUI:
    def __init__(self):
        # Crea el widget ventana
        self.ventana = tkinter.Tk()
        # Crea dos frames, uno para la parte superior de la ventana
        # y otro para la parte inferior
        self.frameSup = Frame(self.ventana)
        self.frameInf = Frame(self.ventana)
        
        # Crea tres widgets label para el frame Superior
        self.label1 = Label(self.frameSup, text = "Uno")
        self.label2 = Label(self.frameSup, text = "Dos")
        self.label3 = Label(self.frameSup, text = "Tres")

        # Llama al método pack para cada widget Label
        self.label1.pack(side = 'top')
        self.label2.pack(side = 'top')
        self.label3.pack(side = 'top')

        # Crea tres wdigets Label para el frame inferior
        self.label4 = Label(self.frameInf, text = "Uno")
        self.label5 = Label(self.frameInf, text = "Dos")
        self.label6 = Label(self.frameInf, text = "Tres")

        # Llama al método pack para cada widget Label
        self.label4.pack(side = 'left')
        self.label5.pack(side = 'left')
        self.label6.pack(side = 'left')

        mainloop()


my_gui = MiGUI()
# Se crea en total cinco objetos
# El constructor init 