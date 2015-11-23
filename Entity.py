from TwitterInterface import *

class Entity(object):
	"""The base object from which all object inherit"""
	def __init__(self):
		self.description = "Description text"
		self.altDescription = " Default Alternate description text"
		self.name = ''

		