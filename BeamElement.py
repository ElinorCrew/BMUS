from MatrixUtil import *
from math import *

class BeamElement:
	def __init__(self, startPoint, endPoint, ID):
		self.start = startPoint
		self.end = endPoint
		self.ID = ID
		self.Type = 'b'
		self.E = 0
		self.I = 0
		self.A = 0

	def getLocalK(self):
		L = self.getLength()
		N = (self.E*self.A)/L
		Y = (self.E*self.I)/pow(L, 3)
		X1 = (self.E*self.I)/pow(L, 2)
		X2 = (self.E*self.I)/L
		localK = [
			[N, 0, 0, -N, 0, 0],
			[0, 12*Y, -6*X1, 0, -12*Y, -6*X1],
			[0, -6*X1, 4*X2, 0, 6*X1, 2*X2],
			[-N, 0, 0, N, 0, 0],
			[0, -12*Y, 6*X1, 0, 12*Y, 6*X1],
			[0, -6*X1, 2*X2, 0, 6*X1, 4*X2]
			]
		return localCToGobalC(setDegreesOfFreedom(localK, appendLists([self.start.degsVector, self.end.degsVector]),),self.getAngel())

	def getLength(self):
		powX = pow((self.end.x - self.start.x), 2)
		powY = pow((self.end.y - self.start.y), 2)
		return sqrt(powX + powY)
		
	def getAngel(self):
		powX = pow((self.end.x - self.start.x), 2)
		powY = pow((self.end.y - self.start.y), 2)
		return atan(powY/powX)
		
	def setPhysicalProperties(self, E, I, A):
		self.E = E
		self.I = I
		self.A = A
		
	def draw(self, canv):
		canv.create_line(self.start.x, self.start.y, self.end.x, self.end.y)
		return canv
		
	def getIdType(self):
		return self.Type + str(self.ID)