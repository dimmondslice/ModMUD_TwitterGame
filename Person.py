from Actor import *

class Person(Actor):
	"""docstring for Person"""
	def __init__(self):
		super(Person, self).__init__()
		self.inventory = None
		self.level = 0
		self.stats = None
		self.gear = None
		self.weapon = None
