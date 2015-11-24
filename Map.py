from Room import *
from Item import Item

import json
class Map(object):
    '''Methods for  saving and loading a Map object from file.
    '''
    def __init__(self):
        super(Map,self).__init__()
        Map.rooms = []
        Map.name = "Test"

    # converts the list of room objects to a json for later use.
    def EncodeMap(self):
        Map.jsonFile = open("resources\\Map.json",'w')
        Map.dictForm = {}
        Map.dictForm['Name'] = Map.name
        Map.dictForm['rooms'] = []
        for x in Map.rooms:
            Map.dictForm['rooms'].append(x.Encode())

        json.dump(Map.dictForm,Map.jsonFile,indent = -1)
        Map.jsonFile.flush()
        Map.jsonFile.close()


    #does the opposite of the above.
    def DecodeJSON(self):
        mapfile = open("resources\\Map.json",'r')
        _dict = json.load(mapfile)
        for room in _dict['rooms']:
            a = Room(_dict = room)
            Map.rooms.append(a)
