from Tkinter import *
from Model import Model

root = Tk()
model = Model()
canvas = Canvas(width=800, height=600, bg='white')
commandText = Text(root, width=100, height=1)
commandText.insert('1.0', "Welcome to BMUS, the interactive truss calculator.")

def drawCanvas(canv, model):
	global commandText
	canv.delete("all")
	model.drawElementList(canv)
	commandText.insert('1.0', model.responseText)

def setPoint(event):
	model.setPoint(event.x, event.y)
	drawCanvas(canvas, model)
	
def setForce(event):
	model.setForce()
	drawCanvas(canvas, model)
	
def setFixture(event):
	model.setFixture()
	drawCanvas(canvas, model)
	
def endPoint(event):
	model.endPoint()
	drawCanvas(canvas, model)
	
def calculate(event):
	endPoint(event)
	model.newCalculation()

root.bind("b", setFixture)
root.bind("f", setForce)
root.bind("c", calculate)

canvas.bind("<Button-1>", setPoint)
canvas.bind("<Button-3>", endPoint)

canvas.pack(expand=YES, fill=BOTH)

commandText.pack(expand=YES, fill=BOTH)

root.mainloop()