from Room import *
import json
class Map(object):
	"""docstring for Map"""
	def __init__(self):
		super(Map,self).__init__()
		Map.rooms = []
		Map.name = "Test"
					# file pointer to a .json
	def GetJSON(self,JSON):
		return json.load(JSON)
	def EncodeMap(self):
		Map.jsonFile = open("resources\\Map.json",'w')
		Map.dictForm = {}
		Map.dictForm['Name'] = Map.name
		Map.dictForm['rooms'] = []
		for x in Map.rooms:
			Map.dictForm['rooms'].append(x.Encode())
		json.dump(Map.dictForm,Map.jsonFile,indent = -1)
	def DecodeJSON(self,_dict):
		for room in _dict['rooms']:
			Map.rooms.append(Room(_dict = room))
			


M = Map()

roomList = []
linklist = []
mapfile = open("resources\\Map.json",'r')
#mapJson = json.load(mapfile)
#A = Room(1)
#B=Room(2)
#C=Room(3)
#
#A.north = "02"
#A.south = "03"
#
#B.south = "01"
#C.north = "01"
#
mapJson = M.GetJSON(mapfile)
#M.rooms.append(A)
#M.rooms.append(B)
#M.rooms.append(C)

#M.EncodeMap()

M.DecodeJSON(mapJson)
for x in M.rooms:
	print x.ID
