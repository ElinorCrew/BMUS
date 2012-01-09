from TestFrame import *
from MatrixUtil import *
from BeamElement import BeamElement
from Point import Point

#Tests
def addOneLocalKTestSmall():
	localKTest = [
		[1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1]
		]
	globalKFinTest = [
		[4, 4, 4, 0, 0, 0],
		[4, 4, 4, 0, 0, 0],
		[4, 4, 4, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0]
		]
	globalKTest = [
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0]
		]
	localIEGTest = [0, 0]
	return assertEqual(addOneLocalK(globalKTest, localKTest, localIEGTest), globalKFinTest)

def addOneLocalKTestMedium():
	localKTest = [
		[11, 21, 31, 41, 51, 61],
		[12, 22, 32, 42, 52, 62],
		[13, 23, 33, 43, 53, 63],
		[14, 24, 34, 44, 54, 64],
		[15, 25, 35, 45, 55, 65],
		[16, 26, 36, 46, 56, 66]
		]
	globalKTest = [
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0]
		]
	localIEGTest = [0, 1]
	return assertEqual(addOneLocalK(globalKTest, localKTest, localIEGTest), localKTest)

def addOneLocalKTestLarge():
	localKTest = [
		[11, 21, 31, 41, 51, 61],
		[12, 22, 32, 42, 52, 62],
		[13, 23, 33, 43, 53, 63],
		[14, 24, 34, 44, 54, 64],
		[15, 25, 35, 45, 55, 65],
		[16, 26, 36, 46, 56, 66]
		]
	globalKFinTest = [
		[11, 21, 31, 0, 0, 0, 41, 51, 61],
		[12, 22, 32, 0, 0, 0, 42, 52, 62],
		[13, 23, 33, 0, 0, 0, 43, 53, 63],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[14, 24, 34, 0, 0, 0, 44, 54, 64],
		[15, 25, 35, 0, 0, 0, 45, 55, 65],
		[16, 26, 36, 0, 0, 0, 46, 56, 66]
		]
	globalKTest = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0]
		]
	localIEGTest = [0, 2]
	return assertEqual(addOneLocalK(globalKTest, localKTest, localIEGTest), globalKFinTest)
	
def calculateSystemMatrixTest():
	beam1 = BeamElement(Point(0, 0, -1), Point(1, 0, -1), -1)
	beam2 = BeamElement(Point(1, 0, -1), Point(2, 0, -1), -1)
	beam1.setPhysicalProperties(1, 1, 1)
	beam2.setPhysicalProperties(1, 1, 1)
	beamList = [beam1, beam2]
	systemMatrix = [
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
	IEG = [[0, 1], [1, 2]]
	numVert = 3
	return assertEqual(calculateSystemMatrix(IEG, beamList, numVert), systemMatrix)

def newNullMatrixTest():
	finNullMatrix = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0]
		]
	testNullMatrix = newNullMatrix(9)
	return assertEqual(finNullMatrix, testNullMatrix)
	
def setDegreesOfFreedomTest():
	matrix = [
		[11, 21, 31, 41, 51, 61],
		[12, 22, 32, 42, 52, 62],
		[13, 23, 33, 43, 53, 63],
		[14, 24, 34, 44, 54, 64],
		[15, 25, 35, 45, 55, 65],
		[16, 26, 36, 46, 56, 66]
		]
	setMatrix = [
		[1, 0, 0, 0, 0, 0],
		[0, 22, 32, 0, 52, 0],
		[0, 23, 33, 0, 53, 0],
		[0, 0, 0, 1, 0, 0],
		[0, 25, 35, 0, 55, 0],
		[0, 0, 0, 0, 0, 1]
		]
	degsVector = [0, 1, 1, 0, 1, 0]
	return assertEqual(setDegreesOfFreedom(matrix, degsVector), setMatrix)
	
def gaussSeidelTest():
	A = [
		[4, 1],
		[1, 4]
		]
	b = [9, 6]
	numSteps = 100
	end = gaussSeidel(A, b, numSteps)
	print end
	return assertEqual(end, end)
	
def gaussSeidelStepTest():
	A = [
		[1, 2, 3],
		[1, 2, 3],
		[1, 2, 3]
		]
	b = [10, 10, 10]
	x0 = [1, 1, 1]
	xn = [4, 0.5, 2*pow(3, -1)]
	return assertEqual(gaussSeidelStep(A, b, x0), xn)
	
def gaussSeidelStepSolitionTest():
	A = [
		[2, 1],
		[5, 2]
		]
	b = [8, 18]
	x0 = [2, 4]
	xn = [0, 5] #Is correct?
	return assertEqual(gaussSeidelStep(A, b, x0), xn)
	
def testForDiagDomTrueTest():
	A = [
		[3, 1, 1],
		[1, 3, 1],
		[0.1, 0.1, 0.3]
		]
	return assertEqual(testForDiagDom(A), True)
	
def testForDiagDomFalseTest():
	A = [
		[3, 1, 4],
		[2, 3, 2],
		[0.1, 0.3, 0.1]
		]
	return assertEqual(testForDiagDom(A), False)
	
def appendListTest():
	listOfLists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	actualList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	return assertEqual(appendLists(listOfLists), actualList)
	
#RunArea
runTest("addOneLocalKTestSmall", addOneLocalKTestSmall())
runTest("addOneLocalKTestMedium", addOneLocalKTestMedium())
runTest("addOneLocalKTestLarge", addOneLocalKTestLarge())
runTest("calculateSystemMatrixTest", calculateSystemMatrixTest())
runTest("newNullMatrixTest", newNullMatrixTest())
runTest("setDegreesOfFreedomTest", setDegreesOfFreedomTest())
runTest("gaussSeidelStepTest", gaussSeidelStepTest())
runTest("gaussSeidelStepSolitionTest", gaussSeidelStepSolitionTest())
runTest("gaussSeidelTest", gaussSeidelTest())
runTest("testForDiagDomTrueTest", testForDiagDomTrueTest())
runTest("testForDiagDomFalseTest", testForDiagDomFalseTest())
runTest("appendListTest", appendListTest())