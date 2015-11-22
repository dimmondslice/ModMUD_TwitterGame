from Command import Command

class Inventory(object):
	"""docstring for Inventory"""
	def __init__(self):
		super(Inventory, self).__init__()
		
		self.grammer = [["inventory"]]

		def Parse(self, words):
			if len(words) == 1:
				#self.twit.SendMessage(message[2],message[1],response,message[0])
				return "printed inventory in console, will update it to do here soon"
			else:
				return "incorrect usage of inventory command"
