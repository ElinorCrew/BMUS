from MatrixUtil import *

class Calculation:
	def __init__(self, IEG, beamList, numVert):
		self.K = calculateSystemMatrix(IEG, beamList, numVert)
		self.displacementVector = []
		self.forceVector = []

	def setForceVector(self, forceVector):
		self.forceVector = forceVector

	def calculateDisplacementVector(self, numIter):
		self.displacementVector = gaussSeidel(self.K, self.forceVector, numIter)