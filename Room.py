from Entity import *
from Player import *

class Room(Entity):
	"""name of room
		Conections to other rooms, will be '00' id there sin't one
		list of people in this room
		list of objects in this room"""
	def __init__(self,_ID= 0,_dict= None):
		super(Room,self).__init__()
		if _dict != None:
			self.Decode(_dict)
		else:
			self.players = None
			self.north= '00'
			self.west= '00'
			self.east= '00'
			self.south= '00'
			self.objects = None
			self.ID = str(_ID).rjust(2,'0')
 
	#Returns each part of the ID, will be somthing different later
	def x(self):
		return int(self.ID[0]) 
	def y(self):
		return int(self.ID[1])

	def Encode(self):
		return self.__dict__
	def Decode(self, _room):
		self.north = _room['north']
		self.south = _room['south']
		self.west = _room['west']
		self.east = _room['east']
		self.ID = _room['ID']
		self.name = _room['name']
		self.objects = _room['objects']
		self.players = _room['players']
		self.description = _room['description']
		self.altDescription = _room['altDescription']