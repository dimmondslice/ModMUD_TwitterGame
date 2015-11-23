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
            self.players = []
            self.neighbors = {
                "north" : "00",
                "west" : "00",
                "east" : "00",
                "south" : "00"
            }
            self.actors = []
            self.ID = str(_ID).rjust(2,'0')

    #Returns each part of the ID, will be somthing different later
    def x(self):
        return int(self.ID[0])
    def y(self):
        return int(self.ID[1])

    def Encode(self):
        return self.__dict__
        # JSON to obj converter
    def RemoveActor(self, _actor):
     	for actor in self.actors:
     		if actor == _actor:
     			self.actors.remove(_actor)
     			break


    def Decode(self, _room):
        self.neighbors = _room['neighbors']
        self.ID = _room['ID']
        self.name = _room['name']
        self.actors = _room['actors']
        self.players = _room['players']
        self.description = _room['description']
        self.altDescription = _room['altDescription']


