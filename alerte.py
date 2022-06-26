import tkinter as tk

class WeeWoo:
	def __init__(self, size=250):
		self.app = tk.Tk()
		self.app.title("Wee-Woo")

		self.size = size
		self.canv = tk.Canvas(self.app, width=size, height=size)
		self.canv.grid()
		self.wee()

		self.app.mainloop()

	def wee(self):
		self.canv.create_rectangle(
			0,0,
			self.size,self.size,
			fill='#f00')
		self.canv.create_rectangle(
			self.size/6,self.size/6,
			(5/6)*self.size,(5/6)*self.size,
			fill='#c00')
		self.canv.create_rectangle(
			self.size/3,self.size/3,
			(2/3)*self.size,(2/3)*self.size,
			fill='#900')
		self.canv.after(200, self.woo)

	def woo(self):
		self.canv.create_rectangle(
			0,0,
			self.size,self.size,
			fill='#900')
		self.canv.create_rectangle(
			self.size/6,self.size/6,
			(5/6)*self.size,(5/6)*self.size,
			fill='#c00')
		self.canv.create_rectangle(
			self.size/3,self.size/3,
			(2/3)*self.size,(2/3)*self.size,
			fill='#f00')
		self.canv.after(1000, self.wee)

if __name__ == "__main__":
	WeeWoo(640)