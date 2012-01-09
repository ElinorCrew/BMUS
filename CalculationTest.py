from TestFrame import *
from BeamElement import BeamElement
from Point import Point
from Calculation import Calculation

#SetUp
beam1 = BeamElement(Point(0, 0), Point(1, 0))
beam2 = BeamElement(Point(1, 0), Point(2, 0))
beam1.setPhysicalProperties(1, 1, 1)
beam2.setPhysicalProperties(1, 1, 1)
beamList = [beam1, beam2]
IEG = [[0, 1], [1, 2]]
numVert = 3
actualK = [
	[1, 0, 0, -1, 0, 0, 0, 0, 0],
	[0, 12, -6, 0, -12, -6, 0, 0, 0],
	[0, -6, 4, 0, 6, 2, 0, 0, 0],
	[-1, 0, 0, 2, 0, 0, -1, 0, 0],
	[0, -12, 6, 0, 24, 0, 0, -12, -6],
	[0, -6, 2, 0, 0, 8, 0, 6, 2],
	[0, 0, 0, -1, 0, 0, 1, 0, 0],
	[0, 0, 0, 0, -12, 6, 0, 12, 6],
	[0, 0, 0, 0, -6, 2, 0, 6, 4]
	]
testCalculation = Calculation(IEG, beamList, numVert)

#Tests
def initTest():
	global actualK
	global testCalculation
	return assertEqual(testCalculation.K, actualK)

def setForceVectorTest():
	global testCalculation
	actualForceVector = [0, 1, 0, 0, 1, 0, 0, 1, 0]
	testCalculation.setForceVector(actualForceVector)
	return assertEqual(testCalculation.forceVector, actualForceVector)

def calculateDisplacementVectorTest():
	global testCalculation
	actualForceVector = [0, 1, 0, 0, 1, 0, 0, 1, 0]
	testCalculation.setForceVector(actualForceVector)
	numIter = 200
	testCalculation.calculateDisplacementVector(numIter)
	actualDisplacementVector = [-0.5, 0.8420386693744827, 0.6323099825540907, -0.5, 0.9440929735773576, 0.6890485549743449, 1.0, 1.3374749554322058, 1.0834055597754169]
	return assertEqual(testCalculation.displacementVector, actualDisplacementVector)

#RunArea
runTest("initTest", initTest())
runTest("setForceVectorTest", setForceVectorTest())
runTest("calculateDisplacementVectorTest", calculateDisplacementVectorTest())