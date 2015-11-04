from Room import *
class Map(object):
	"""docstring for Map"""
	def __init__(self):
		super(Map,self).__init__()
		
		Map.rooms = []
		Map.name = ""
	def GenRooms(JSON):
		pass


a = Room()
a.description = "Test Room"
b = Room()
b.description = "Test Room 2"

a.north = b
b.north = a
M = Map()
P = Map()



M.rooms.append(a)
M.rooms.append(b)

M.name += "Not Blah"
print P.rooms[0].north.description
print M.rooms[1].north.description

print P.name
print M.name