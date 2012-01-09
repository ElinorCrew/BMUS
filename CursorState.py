class CursorState:
	def __init__(self):
		self.pointState = True
		self.forceState = False
		self.fixtureState = False
		self.modeText = "Mode: set point\n"
	
	def setPointState(self):
		self.pointState = True
		self.forceState = False
		self.fixtureState = False
		self.modeText = "Mode: set point\n"
	
	def setForceState(self):
		self.pointState = False
		self.forceState = True
		self.fixtureState = False
		self.modeText = "Mode: set force\n"
	
	def setFixtureState(self):
		self.pointState = False
		self.forceState = False
		self.fixtureState = True
		self.modeText = "Mode: set fixture\n"
		