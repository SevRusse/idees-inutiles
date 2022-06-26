import tkinter as tk
from math import cos,sin,pi

class Fractale:
	def __init__(self, d=3, size=640):
		self.app = tk.Tk()
		self.app.title("Fractales triangulaires")
		self.app.bind()

		self.size = size
		self.canv = tk.Canvas(self.app, width=size, height=size)
		self.canv.grid()

		x1,y1 = (size/2)+(size/3)*cos(-pi/2),(size/2)+(size/3)*sin(-pi/2)
		x2,y2 = (size/2)+(size/3)*cos(5*pi/6),(size/2)+(size/3)*sin(5*pi/6)
		x3,y3 = (size/2)+(size/3)*cos(pi/6),(size/2)+(size/3)*sin(pi/6)
		self.Fractale(d, x1,y1, x2,y2, x3,y3)

		self.app.mainloop()

	def Fractale(self, depth, x1,y1, x2,y2, x3,y3):
		"""Dessine une fractale de profondeur depth contenue dans la fractale de profondeur superieure."""
		self.canv.create_line(x1,y1, x2,y2)
		self.canv.create_line(x2,y2, x3,y3)
		self.canv.create_line(x3,y3, x1,y1)
		self.app.update()
		if depth > 0:
			# A est le milieu du segment opposé à p1
			xa,ya = milieu(x2,y2, x3,y3)
			# B est le milieu du segment opposé à p2
			xb,yb = milieu(x1,y1, x3,y3)
			# C est le milieu du segment opposé à p3
			xc,yc = milieu(x1,y1, x2,y2)
			self.Fractale(depth-1, x1,y1, xb,yb, xc,yc)
			self.Fractale(depth-1, xa,ya, x2,y2, xc,yc)
			self.Fractale(depth-1, xa,ya, xb,yb, x3,y3)

def milieu(x1,y1, x2,y2):
	"""Retourne le point p3(x3,y3), milieu du segment 2D entre p1(x1,y1) et p2(x2,y2)."""
	return ((x1+x2)/2,(y1+y2)/2)

if __name__ == "__main__":
	Fractale(7)
