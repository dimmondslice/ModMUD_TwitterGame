include Entity

class Actor (Entity):
	"""All things that can exist in the world"""
	def __init__(self, arg):
		super(Actor , self).__init__()
		self.canGrab = false

		