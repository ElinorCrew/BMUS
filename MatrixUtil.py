from math import *
#simen var her
def addOneLocalK(globalK, localK, localIEG):
	localLen = len(localK)
	localPiv = floor(localLen/2)
	u = localIEG[0]*3
	v = -3 + localIEG[1]*3
	
	for i in range(localLen):
		for j in range(localLen):
			if i<localPiv and j<localPiv:
				globalK[i+u][j+u] += localK[i][j]
			elif i<localPiv and j>=localPiv:
				globalK[i+u][j+v] += localK[i][j]
			elif i>=localPiv and j<localPiv:
				globalK[i+v][j+u] += localK[i][j]
			else:
				globalK[i+v][j+v] += localK[i][j]
	return globalK

def calculateSystemMatrix(IEG, beamList, numVert):
	tempK = newNullMatrix(numVert*3)
	for i in range(len(IEG)):
		addOneLocalK(tempK, beamList[i].getLocalK(), IEG[i])
	return tempK

def newNullMatrix(lenK):
		newMatrix = []
		for i in range(lenK):
			row = []
			for i in range(lenK):
				row.append(0.0)
			newMatrix.append(row)
		return newMatrix
		
def setDegreesOfFreedom(matrix, degsVector):
	if degsVector == []:
		return matrix
	for i in range(len(matrix)):
		if degsVector[i] == 0:
			for j in range(len(matrix)):
				if i == j:
					matrix[i][j] = 1
				else:
					matrix[i][j] = 0
					matrix[j][i] = 0
	return matrix
	
def gaussSeidel(A, b, numSteps):
	if testForDiagDom(A) == False:
		print "Linear system is not diagonally dominant. Convergence is not gauranteed."
	x0 = getTestX(A, b)
	for n in range(numSteps):
		x1 = gaussSeidelStep(A, b, x0)
		x0 = x1
	return x0

def testForDiagDom(matrix):
	diagonalElement = matrix[0][0]
	for i in range(len(matrix[0])):
		rowSum = 0
		for j in range(len(matrix[0])):
			if i == j:
				diagonalElement = matrix[i][j]
			else:
				rowSum += matrix[i][j]
		if abs(rowSum) > abs(diagonalElement):
			return False
	return True
	
def getTestX(A, b):
	x = []
	for i in range(len(b)):
		x.append(1)
	return x
	
def gaussSeidelStep(A, b, x0):
	x1 = []
	for i in range(len(b)):
		tempX1 = elementGauss(A, b, x0, x1, i)
		x1.append(tempX1)
	return x1

def elementGauss(A, b, x0, x1, i):
	LUCorrFactor = pow(A[i][i], -1)
	sumAX0 = sum(vectorMultiply(A[i], x0, i, len(x0)))
	sumAX1 = sum(vectorMultiply(A[i], x1, 0, i))
	return LUCorrFactor*(b[i]-sumAX0-sumAX1)

def vectorMultiply(V1, V2, n, m):
	tempVector = []
	for i in range(n, m):
		tempVector.append(V1[i]*V2[i])
	return tempVector
	
def appendLists(listOfLists):
	newList = []
	for liste in listOfLists:
		for element in liste:
			newList.append(element)
	return newList