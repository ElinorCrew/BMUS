from Model import Model
from CursorState import CursorState
from Tkinter import *

root = Tk()
model = Model()
cursorState = CursorState()
canvas = Canvas(width=800, height=600, bg='white')
commandText = Text(root, width=100, height=1)
commandText.insert('1.0', cursorState.modeText)

def doCursorAction(event):
	if cursorState.pointState:
		model.setPoint(event.x, event.y)
	elif cursorState.forceState:
		model.setForce(event.x, event.y)
	elif cursorState.fixtureState:
		model.setFixture()
	drawCanvas(canvas, model)

def drawCanvas(canv, model):
	canv.delete("all")
	model.drawElementList(canv)

def setPoint(event):
	cursorState.setPointState()
	commandText.insert('1.0', cursorState.modeText)
	
def setForce(event):
	cursorState.setForceState()
	commandText.insert('1.0', cursorState.modeText)
	
def setFixture(event):
	canvas.gettags("current")
	cursorState.setFixtureState()
	commandText.insert('1.0', cursorState.modeText)
	
def endPoint(event):
	model.endPoint()
	drawCanvas(canvas, model)
	
def calculate(event):
	endPoint(event)
	model.newCalculation()

root.bind("s", setPoint)
root.bind("f", setForce)
root.bind("b", setFixture)
root.bind("c", calculate)
root.bind("e", endPoint)

canvas.bind("<Button-1>", doCursorAction)

canvas.pack(expand=YES, fill=BOTH)
commandText.pack(expand=YES, fill=BOTH)
root.mainloop()