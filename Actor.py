from Entity import *

class Actor(Entity):
	"""All things that can exist in the world"""
	def __init__(self):
		super(Actor,self).__init__()
		self.canGrab = False
		self.location = None
		self.commands = []

