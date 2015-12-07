from Entity import Entity
from Player import *
from Item import Item
from Actor import Actor

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
        myDict = self.__dict__
        actorDicts = []
        for x in self.actors:
            actorDicts.append(x.Encode())

        myDict["actors"] = actorDicts

        return myDict
        # JSON to obj converter
    def RemoveActor(self, _actor):
        for actor in self.actors:
            if actor == _actor:
                self.actors.remove(_actor)
                break
    def AddActor(self, _actor):
        self.actors.append(_actor)
        _actor.location = self


        # Stores objs in a JSON format for ease of saving and reading.
    def Decode(self, _room):
        self.neighbors = _room['neighbors']
        self.ID = _room['ID']
        self.name = _room['name']
        self.players = _room['players']
        self.description = _room['description']
        self.altDescription = _room['altDescription']
        #redefine the actors list and populate it from data in the json
        self.actors = []
        for actor in _room['actors']:
            dummy = Actor(actor)
            dummy.location = self
            self.actors.append(dummy)


