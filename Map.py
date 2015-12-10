from Room import Room
from Item import Item
import json
from Singleton import Singleton

@Singleton
class Map(object):
    '''Methods for  saving and loading a Map object from file.
    '''
    def __init__(self):
        #super(Map,self).__init__()
        self.rooms = []
        self.name = "Test"

    # converts the list of room objects to a json for later use.
    def EncodeMap(self):
        self.jsonFile = open("resources\\JailMap.json",'w')
        self.dictForm = {}
        self.dictForm['Name'] = self.name
        self.dictForm['rooms'] = []
        for x in self.rooms:
            self.dictForm['rooms'].append(x.Encode())
        json.dump(self.dictForm,self.jsonFile,indent = -1)
        self.jsonFile.flush()
        self.jsonFile.close()


    #does the opposite of the above.
    def DecodeJSON(self):
        mapfile = open("resources\\JailMap.json",'r')
        _dict = json.load(mapfile)
        for room in _dict['rooms']:
            a = Room(_dict = room)
            self.rooms.append(a)

    def GetRoomByID(self, ID):
        for room in self.rooms:
            if room.ID == ID:
                return room
