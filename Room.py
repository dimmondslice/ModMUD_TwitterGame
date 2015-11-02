'''
name of room

room.n bool hasDoor if yes
room.s
room.w
room.e



Conections to other rooms
list of people in this room
list of objects in this room

Map Class:
	List of rooms
	gen all rooms
	Base it on JSON
	
'''

from Entity import *
from Player import *

class Room(Entity):
	"""name of room
		Conections to other rooms, will be None is there isn't one
		list of people in this room
		list of objects in this room"""
	def __init__(self):
		super(Room,self).__init__()
		self.players = None
		self.north= None
		self.south= None
		self.east= None
		self.west= None
		self.objects = None
		self.ID = None
		self.name = "A Room"
 		


