from Actor import *

class Item(Actor):
	"""Anything that can be put into the players inventory or equipped"""
	def __init__(self):
		super(Item, self).__init__()
