from Room import *
class Map(object):
	"""docstring for Map"""
	def __init__(self):
		super(Map,self).__init__()
		
		Map.rooms = []
		Map.name = ""
	def GenRooms(JSON):
		pass



roomList = []
linklist = []



 		
for x in range(0,6):
	templist = []
	for y in range(0,6):
		temp = Room()
		temp.ID = str(x)+str(y)
		temp.name = "Room " +temp.ID
		linklist.append(temp)
		templist.append(temp)
	roomList.append(templist)
q = 0
for i in linklist:
	for j in linklist:
		if i !=j:
			if int(i.ID) == (int(j.ID) - 1):
				i.east = j
				j.west = i
				#print "E/W Made"
			if int(i.ID) == (int(j.ID) - 10):
				i.south = j
				j.north = i
				#print "N/S Made"


for x in range(0,6):
	for y in range(0,6):
		#print str(roomList[x][y].x()) + str(roomList[x][y].y()),
		pass
	#print


for item in roomList:
	for item2 in item:
		print item2.name,
	print
