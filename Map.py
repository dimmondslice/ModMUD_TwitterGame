from Room import *
import json
class Map(object):
	"""docstring for Map"""
	def __init__(self):
		super(Map,self).__init__()
		Map.jsonFile = open("resources\\Map.json",'w')
		Map.rooms = []
		Map.name = ""
	def GenRooms(self,JSON):
		pass
	def EncodeMap(self):
		Map.dictForm = {}
		Map.dictForm['Name'] = Map.name
		Map.dictForm['rooms'] = []
		for x in Map.rooms:
			Map.dictForm['rooms'].append(x.encode())
		json.dump(Map.dictForm,Map.jsonFile,indent = -1)


roomList = []
linklist = []
#mapfile = open("resources\\Map.json")
#mapJson = json.load(mapfile)
#ID = '00'
#for x in mapJson['rooms']:
#	print x
#	temp = Room()
#	temp.name = x["Name"]
#	temp.west = x["Rooms"]["West"]
#	temp.north = x["Rooms"]["North"]
#	temp.east = x["Rooms"]["East"]
#	temp.south = x["Rooms"]["South"]
#	linklist.append(temp)
#print linklist[0].north

A = Room(1)
B=Room(2)
C=Room(3)
M = Map()

M.rooms.append(A)
M.rooms.append(B)
M.rooms.append(C)

M.EncodeMap()
#
#for x in range(0,6):
#	templist = []
#	for y in range(0,6):
#		temp = Room()
#		temp.ID = str(x)+str(y)
#		temp.name = "Room " +temp.ID
#		linklist.append(temp)
#		templist.append(temp)
#	roomList.append(templist)
#q = 0
#for i in linklist:
#	for j in linklist:
#		if i !=j:
#			if int(i.ID) == (int(j.ID) - 1):
#				i.east = j
#				j.west = i
#				#print "E/W Made"
#			if int(i.ID) == (int(j.ID) - 10):
#				i.south = j
#				j.north = i
#				#print "N/S Made"
#
#
#for x in range(0,6):
#	for y in range(0,6):
#		#print str(roomList[x][y].x()) + str(roomList[x][y].y()),
#		pass
#	#print


for item in roomList:
	for item2 in item:
		print item2.name,
	print
