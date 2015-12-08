from Actor import *
from Item import Item

class Person(Actor):
	"""docstring for Person"""
	def __init__(self):
		super(Person, self).__init__()
		self.inventory = []
		self.InventoryInit()
		self.level = 0
		self.stats = None
		self.gear = None
		self.weapon = None
	#just used to put a couple items in the persons inventory
	def InventoryInit(self):
		#pass
		key = Item("Mysterious Key")
		self.inventory.append(key)
	def PrintInventory(self):
		response = "Stuff in your inventory:\n" 
		for i in self.inventory:
			response += "...." + i.name + '\n '
		return response
	def AddToInventory(self, _actor):
		self.inventory.append(_actor)