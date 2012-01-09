from Tkinter import *
from Model import Model

root = Tk()
model = Model()
canvas = Canvas(width=800, height=600, bg='white')
commandLine = Canvas(width=800, height=30, bg='gray')

def drawCanvas(canv, commandLine, model):
	canv.delete("all")
	commandLine.delete("all")
	model.drawElementList(canv)
	commandLine.create_text(400, 15, text=model.responseText)

def setPoint(event):
	model.setPoint(event.x, event.y)
	drawCanvas(canvas, commandLine, model)
	
def setForce(event):
	model.setForce()
	drawCanvas(canvas, commandLine, model)
	
def setFixture(event):
	model.setFixture()
	drawCanvas(canvas, commandLine, model)
	
def endPoint(event):
	model.endPoint()
	drawCanvas(canvas, commandLine, model)
	
def calculate(event):
	endPoint(event)
	model.newCalculation()

root.bind("b", setFixture)
root.bind("f", setForce)
root.bind("c", calculate)

canvas.bind("<Button-1>", setPoint)
canvas.bind("<Button-3>", endPoint)

canvas.pack(expand=YES, fill=BOTH)
commandLine.create_text(400, 15, text=model.responseText)
commandLine.pack(expand=YES, fill=BOTH)

root.mainloop()