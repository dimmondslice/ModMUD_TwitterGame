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
		key = Item("Mysterious Key")
		self.inventory.append(key)
	def PrintInventory(self):
		print("printing inventory for " + self.name)
		for i in self.inventory:
			print(i.name)
