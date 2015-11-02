from Person import *
from Go import Go
from Tweet import Tweet

class Player(Person):
	"""docstring for Player"""
	def __init__(self):
		super(Player, self).__init__()
		self.verbContext = {
			"go" : Go(),
			"tweet" : Tweet()
		}
		self.twitterID = ""

							#input string
	def ParseMessage(self, message):
		words = message.lower().split()
		if words[0] in self.verbContext:
			self.verbContext[words[0]].Parse(words)
		else:
			print(words[0] + " is not a recognized command")

