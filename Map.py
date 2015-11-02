from Room import *
class Map(object):
	"""docstring for Map"""
	def __init__(self):
		super(Map,self).__init__()
		self.rooms = []
		

a = Room()
a.description = "Test Room"
b = Room()
b.description = "Test Room 2"

a.north = b
M = Map()

M.rooms.append(a)
M.rooms.append(b)

print M.rooms[0].north.description

