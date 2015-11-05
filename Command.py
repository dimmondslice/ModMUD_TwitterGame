from Entity import *

class Command(Entity):
	"""docstring for Command"""
	def __init__(self):
		super (Command, self).__init__()
		self.Grammer = [[]]

					#list of strings
	def Parse(self, words):
		return "Yo you should have overloaded Command.Parse()"



		