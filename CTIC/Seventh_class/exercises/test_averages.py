from tkinter import Tk, Frame, Label, Entry, LEFT, mainloop, StringVar, Button

class TestAvg:
	def __init__(self):
		self.main_window = Tk()
		self.main_window.title("Calcula Promedios")

		self.test1_frame = Frame(self.main_window)
		self.test2_frame = Frame(self.main_window)
		self.test3_frame = Frame(self.main_window)
		self.avg_frame = Frame(self.main_window)
		self.button_frame = Frame(self.main_window)

		self.test1_label = Label(self.test1_frame, text = "Enter the score for test 1: ")
		self.test1_entry = Entry(self.test1_frame, width = 10)
		self.test1_label.pack(side = LEFT)
		self.test1_entry.pack(side = LEFT)

		self.test2_label = Label(self.test2_frame, text = "Enter the score for test 2: ")
		self.test2_entry = Entry(self.test2_frame, width = 10)
		self.test2_label.pack(side = LEFT)
		self.test2_entry.pack(side = LEFT)

		self.test3_label = Label(self.test3_frame, text = "Enter the score for test 3: ")
		self.test3_entry = Entry(self.test3_frame, width = 10)
		self.test3_label.pack(side = LEFT)
		self.test3_entry.pack(side = LEFT)

		self.result_label = Label(self.avg_frame, text = "Average")
		self.avg = StringVar() # To update avg_label
		self.avg_label = Label(self.avg_frame, textvariable = self.avg)
		self.result_label.pack(side = LEFT)
		self.avg_label.pack(side = LEFT)

		self.calc_button = Button(self.button_frame, text = "Average", command = self.calc_avg)
		self.quit_button = Button(self.button_frame, text = "Quit", command = self.main_window.destroy)

		self.calc_button.pack(side = LEFT)
		self.quit_button.pack(side = LEFT)

		self.test1_frame.pack()
		self.test2_frame.pack()
		self.test3_frame.pack()
		self.avg_frame.pack()
		self.button_frame.pack()

		mainloop()
	
	def calc_avg(self):
		self.test1 = float(self.test1_entry.get())
		self.test2 = float(self.test2_entry.get())
		self.test3 = float(self.test3_entry.get())

		self.average = (self.test1 + self.test2 + self.test3) / 3
		self.avg.set(self.average)


test_avg = TestAvg()
mainloop()