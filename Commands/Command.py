from Entity import *

class Command(Entity):
	"""docstring for Command"""
	def __init__(self):
		super (Command, self).__init__()
		self.verb = ""
					#list of strings
	def Parse(self, words):
		if words[0] != self.verb:
			print("yo wtf")



		