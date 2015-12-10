from Actor import Actor
from Map import Map

class CellDoor(Actor):
    """docstring for CellDoor"""
    def __init__(self, _dict = None):
        super(CellDoor, self).__init__()
        if _dict != None:
            self.Decode(_dict)
        else:
            self.name = "unnamed cell door"
            #of the form ["direction door leads", ID of room the door leads to]
            self.adjacentRoom = None
            #self.adjacentRoomID = 0

    #cell door's use function will unlock the door if the player uses the right key on it, then it will reinstate the connection between the room
    #that contains this door, and the adjacent room
    def Use(self, _actorUsedWith):
        if("cell" in _actorUsedWith.name and "key" in _actorUsedWith):
            #now re enable the neighbor connections
            self.location.neighbors[self.adjacentRoom[0]] = self.adjacentRoom[1]
            neighborRoom = Map.Instance().GetRoombyID(self.adjacentRoom[1])
            #to to the neighbor room and re enable its connection to this room
            neighborRoom.neighbors[self.OppositeDir(_dict["adjacentRoom"])] = self.location.ID

    def Decode(self, _dict):
        super(CellDoor, self).Decode(_dict)

        #now is when I will actually set self.adjecentRoom, bc I can garauntee I know self.location now

        roomID = self.location.neighbors[ _dict["adjacentRoom"]]
        #within the code,unlike the JSON, self.adjacentRoom is actually a list in the form ["direction this door leads to", id of that room]
        self.adjacentRoom = [ _dict["adjacentRoom"], roomID]
        #now disable the neighbor connections
        neighborID = self.location.neighbors[_dict["adjacentRoom"]]
        neighborRoom = Map.Instance().GetRoomByID(neighborID)
        #gross thing then just returns the opposite direction of the one given is used to turn off the "other side of this door"
        neighborRoom.neighbors[self.OppositeDir(_dict["adjacentRoom"])] = 0
        neighborID = 0  #have this rooms neighbor point to nothing

    def OppositeDir(self, _dir):
        _dir = _dir.lower()
        if _dir == "north":
            return "south"
        elif _dir == "south":
            return "north"
        elif _dir == "west":
            return "east"
        elif _dir == "east":
            return "west"

    def Encode(self):
        #we're not calling actor encode, so we also need to not encode the location
        myDict = self.__dict__
        myDict["adjacentRoom"] = self.adjacentRoom[0]
        myDict['location'] = None
        return myDict