from IdState import IdState
from Calculation import Calculation
from BeamElement import BeamElement
from Point import Point

from MatrixUtil import *
from TestFrame import *

class Model:
	def __init__(self):
		self.elementList = []
		self.idState = IdState()
		self.setPointState = False
		
	def setPoint(self, x, y):
		pointB = Point(x, y, self.idState.getPointId())
		if self.setPointState and (0 != len(self.elementList)):
			pointA = self.elementList.pop()
			beamElement = BeamElement(pointA, pointB, self.idState.getBeamId())
			self.elementList.append(beamElement)
			self.elementList.append(pointA)
		self.elementList.append(pointB)
		self.setPointState = True
		
	def endPoint(self):
		self.setPointState = False
		
	def setForce(self, x, y):
		index = self.getSelectedElementIndex(x, y)
		if index != -1 and self.elementList[index].Type == 'p':
			self.elementList[index].addForce();
		self.setPointState = False
	
	def setFixture(self, x, y):
		self.setPointState = False
		
	def drawElementList(self, canv):
		for element in self.elementList:
			element.draw(canv)
		return canv
	
	def getSelectedElementIndex(self, x, y):
		for i in range(len(self.elementList)):
			if self.elementList[i].isSelected(x, y):
				return i
		return -1
		
	def newCalculation(self):
		newCalculation = Calculation(self.calculateIEG(), self.getBeamList(), self.calculateNumVert())
		#TODO: Get force vector from user and number of iterations from user..
		newCalculation.setForceVector(self.getForceVector())
		newCalculation.calculateDisplacementVector(200)
		
		print "Stivhetsmatrise:"
		printC(newCalculation.K)
		print "Forskyvningsvektor:"
		print newCalculation.displacementVector
		print "Belastningsvektor:"
		print newCalculation.forceVector
		
	def calculateIEG(self):
		IEG = []
		for element in self.elementList:
			if element.Type == 'b':
				IEG.append([element.start.ID, element.end.ID])
		return IEG
		
	def calculateNumVert(self):
		numVert = 0
		for element in self.elementList:
			if element.Type == 'p':
				numVert += 1
		return numVert
		
	def getBeamList(self):
		beamList = []
		for element in self.elementList:
			if element.Type == 'b':
				#TODO: User set properties.
				element.setPhysicalProperties(1, 1, 1)
				beamList.append(element)
		return beamList
		
	def getForceVector(self):
		localForceVectors = []
		for element in self.elementList:
			if element.Type == 'p':
				localForceVectors.append(element.forceVector)
		return appendLists(localForceVectors)
		
	def printElementListId(self):
		liste = []
		for element in self.elementList:
			liste.append(element.getIdType())
		print liste