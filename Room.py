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
	def __init__(self,_ID):
		super(Room,self).__init__()
		self.players = None
		self.north= '00'
		self.west= '00'
		self.east= '00'
		self.south= '00'
		self.objects = None
		self.ID = str(_ID).rjust(2,'0')
 

	def x(self):
		return int(self.ID[0]) 
	def y(self):
		return int(self.ID[1])

	def encode(self):
		return self.__dict__

