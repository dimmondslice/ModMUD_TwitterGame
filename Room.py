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
		self.ID = '00'
		self.name = "A Room"
 

	def x(self):
		return int(self.ID[0]) 
	def y(self):
		return int(self.ID[1])

roomList = []



 		
for x in range(0,6):
	templist = []
	for y in range(0,6):
		temp = Room()
		temp.ID = str(x)+str(y)
		templist.append(temp)
	roomList.append(templist)
q = 0
#for i in roomList:
#	for j in roomList:
#		if i !=j:
#			if int(i.ID) == (int(j.ID) - 1):
#				i.east = j
#				j.west = i
#				#print "E/W Made"
#			if int(i.ID) == (int(j.ID) - 10):
#				i.south = j
#				j.north = i
#				#print "N/S Made"


for x in range(0,6):
	for y in range(0,6):
		print str(roomList[x][y].x()) + str(roomList[x][y].y()),
	print


