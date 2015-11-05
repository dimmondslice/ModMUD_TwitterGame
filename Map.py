from Room import *
import json
class Map(object):
	"""docstring for Map"""
	def __init__(self):
		super(Map,self).__init__()
		Map.rooms = []
		Map.name = "Test"
					# file pointer to a .json used for testing 
	def GetJSON(self,JSON):
		'''Get a dict from a .json, mostly used to debug right now. '''
		return json.load(JSON)
	# converts the list of room objects to a json for later use.
	def EncodeMap(self):
		Map.jsonFile = open("resources\\Map.json",'w')
		Map.dictForm = {}
		Map.dictForm['Name'] = Map.name
		Map.dictForm['rooms'] = []
		for x in Map.rooms:
			Map.dictForm['rooms'].append(x.Encode())
		json.dump(Map.dictForm,Map.jsonFile,indent = -1)
		#does the opposite of the above.
	def DecodeJSON(self,_dict):
		for room in _dict['rooms']:
			Map.rooms.append(Room(_dict = room))
			


M = Map()

mapfile = open("resources\\Map.json",'r')
mapJson = M.GetJSON(mapfile)

M.DecodeJSON(mapJson)
for x in M.rooms:
	print x.ID
