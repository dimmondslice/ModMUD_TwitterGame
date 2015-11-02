from Command import Command

class Go (object):
	"""You use this to go"""
	def __init__(self, arg):
		super(Go, self).__init__()
		self.arg = arg
					#list of strings
	def Parse(self, words):
		super(Go, self).Parse(words)
		print("You went " + words[1])

