from Actor import Actor

class KeyHalf(Actor):
	"""docstring for KeyHalf"""
	def __init__(self, _dict = None):
		super(KeyHalf, self).__init__(_dict)
		self.name ="CellKey A FrontHalf"

		self.otherHalf = ""
		if("Front" in self.name):
			self.otherHalf = self.name.replace("Front", "Back")
		elif("Back" in self.name):
			self.otherHalf = self.name.replace("Back", "Front")