from Entity import Entity
from Item import Item
from Actor import Actor
from pydoc import locate

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
                "north" : 0,
                "west" : 0,
                "east" : 0,
                "south" : 0
            }
            self.actors = []
            self.ID = 0

    def Encode(self):
        myDict = self.__dict__
        actorDicts = []
        playerDicts = []
        numPlayer = len(self.players)
        print numPlayer
        for x in self.actors:
            actorDicts.append(x.Encode())
        for x in self.players:

            if x not in playerDicts:
                playerDicts.append(x.Encode())

        myDict["actors"] = actorDicts
        myDict["players"] = playerDicts

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
        #print _room
        self.neighbors = _room['neighbors']
        self.ID = _room['ID']
        self.name = _room['name']
        self.players = []
        self.description = _room['description']
        self.altDescription = _room['altDescription']
        #redefine the actors list and populate it from data in the json
        self.actors = []
        for actorDict in _room['actors']:
            if(actorDict["type"]=="CellDoor"):
                print("about to decode celldoor")
                from CellDoor import CellDoor
                #it's important that we call the constructor with out passing it the actorDict, that way the decode happens after the location is set
                dummy = locate(actorDict["type"]).CellDoor()
                dummy.location = self
                dummy.Decode(actorDict)
                self.actors.append(dummy)
                del CellDoor
            elif(actorDict["type"]=="KeyHalf"):
                from KeyHalf import KeyHalf
                print("about to decode key")
                #it's important that we call the constructor with out passing it the actorDict, that way the decode happens after the location is set
                dummy = locate(actorDict["type"]).KeyHalf()
                dummy.location = self
                dummy.Decode(actorDict)
                self.actors.append(dummy)
                del KeyHalf
            else:
                dummy = Actor(actorDict)
                dummy.location = self
                self.actors.append(dummy)
        #print "decoding player"

        from Player import Player
        for player in _room['players']:
            dummy = Player(_dict = player)
            dummy.location = self
            self.players.append(dummy)
        #print "Number of players in room "+ str(len(self.players))


