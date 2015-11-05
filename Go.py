from Command import Command

class Go (Command):
	"""You use this to go"""
	def __init__(self):
		super(Go, self).__init__()
					#list of strings
		self.Grammer = [["go"],["north","south","east","west","poop"]]
	def Parse(self, words):
		if len(words) < 2:
			return 'improper use of "go" command'
		elif words[1]:
			return "Please don't do that here"
		elif words[1] in self.Grammer[1]:
			return "You went " + words[1]
		else:
			return '"' +words[1] + "\" is not a recognized direction"

