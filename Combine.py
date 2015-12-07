from Combine import Combine

class Combine(Command):
	"""docstring for Combine"""
	def __init__(self):
		super(Combine, self).__init__()
		
		self.name = "combine"
		self.grammer = [["combine"],[],["with"],[]]
	
