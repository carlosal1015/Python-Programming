#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import Tk, Frame, Label, mainloop, Button, LEFT, StringVar
from random import randint as rd

class Random_GUI:
	def __init__(self):
		self.main_window = Tk()
		self.main_window.title("Calculadora aleatoria: suma, máximo y mínimo.")
		self.main_window.geometry("500x100")

		self.test1_frame = Frame(self.main_window)
		self.test2_frame = Frame(self.main_window)
		self.test3_frame = Frame(self.main_window)

		self.random_button = Button(self.test1_frame, text = "Generar número aleatorios entre 0 y 9: ", command = self.random_generator)
		self.random_button.pack(side = LEFT)
		self.summation_button = Button(self.test2_frame, text = "Mostrar la suma: ")
		self.summation_button.pack(side = LEFT)
		self.maximum_minimum = Button(self.test3_frame, text = "Mostrar el máximo y mínimo: ")
		self.maximum_minimum.pack(side = LEFT)

		self.random_list = StringVar()
		self.test1_label = Label(self.test1_frame, textvariable = self.random_list)
		self.test1_label.pack(side = LEFT)

		self.print_summation = StringVar()
		self.test2_label = Label(self.test2_frame, textvariable = self.print_summation)
		self.test2_label.pack(side = LEFT)

		self.print_max_min = StringVar()
		self.test3_label = Label(self.test3_frame, textvariable = self.print_max_min)
		self.test3_label.pack(side = LEFT)

		self.test1_frame.pack()
		self.test2_frame.pack()
		self.test3_frame.pack()

		mainloop()


	def random_generator(self):
		self.list_random = [rd(0, 9) for i in range(10)]
		self.new_list_random = " ".join(str(j) for j in self.list_random)
		self.random_list.set(self.new_list_random)

		self.summation = sum(self.list_random)
		self.print_summation.set(self.summation)

		self.maximum = max(self.list_random)
		self.minimum = min(self.list_random)
		self.max_min = "El máximo es: " + str(self.maximum) + " y el mínimo es " + str(self.minimum)
		self.print_max_min.set(self.max_min)


test_random_gui = Random_GUI()