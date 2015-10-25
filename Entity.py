class Entity(object):
	"""The base object from which all object inherit"""
	def __init__(self, _name):
		super(Entity, self).__init__()

		self.name = _name
		self.description = "Description text"
		self.altDescription = " Default Alternate description text"

		