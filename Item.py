include Actor

class Item(Actor):
	"""Anything that can be put into the players inventory or equipped"""
	def __init__(self, arg):
		super(Item, self).__init__()
