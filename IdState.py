class IdState:
	def __init__(self):
		self.lineId = -1
		self.pointId = -1
		
	def getBeamId(self):
		self.lineId += 1
		return self.lineId
		
	def getPointId(self):
		self.pointId += 1
		return self.pointId