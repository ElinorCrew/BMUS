class Point:
	def __init__(self, x, y, ID):
		self.x = x
		self.y = y
		self.rad = 5
		self.ID = ID
		self.Type = 'p'
		self.forceVector = [0, 0, 0]
		self.degsVector = [1, 1, 1]
		
	def draw(self, canv):
		canv.create_oval(self.x-self.rad,self.y-self.rad,self.x+self.rad,self.y+self.rad,width=0,fill='grey')
		return canv
		
	def isSelected(self, x, y):
		return self.x-x < self.rad and self.x-x > -self.rad and self.y-y <self.rad and self.y-y > -self.rad
		
	def getIdType(self):
		return self.Type + str(self.ID)