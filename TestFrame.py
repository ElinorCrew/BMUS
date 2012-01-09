def assertEqual(x, y):
	return x==y
	
def runTest(name, test):
	print name + ": " + str(test)

def printC(matrix):
	print "["
	for row in matrix:
		outStr = "["
		for element in row:
			outStr += str(element) + ", "
		outStr += "]"
		print outStr
	print "]"