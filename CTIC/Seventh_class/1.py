#from tkinter import Tk as tk
from tkinter import *

windows = Tk()
windows.title = "Mi primer programa GUI!"
windows = Tk()
windows.title = "Mi primer programa GUI!"
windows.geometry("400x400")
windows.mainloop()
windows.configure(background = "lightblue")
label = Label(windows,
    text = "Bienvenido a Python!",
    bg = "yellow",
    fg = "purple1",
    font = ("Mistral", 14))

# Existen hasta tres gestores de geometria. Hoy usaremos pack.
label.pack() # Gestor de geometria que posiciona el objeto contenedor