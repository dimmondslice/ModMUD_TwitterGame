from Actor import *

class Item(Actor):
	"""Anything that can be put into the players inventory or equipped"""
	def __init__(self, _name = "generic item"):
		super(Item, self).__init__()		
		self.name = _name
