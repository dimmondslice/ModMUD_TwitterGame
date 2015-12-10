from Entity import *

class Actor(Entity):
    """All things that can exist in the world"""
    def __init__(self, _dict = None):
        if _dict != None:
            self.Decode(_dict)
        else:
            super(Actor,self).__init__()
            self.location = None
            #self.commands = []
            self.takeable = True
            #
            self.type = "Actor"
    '''
    Allows saving Actors to json as well as creating objects from a json file.
    '''
    def Decode(self, _dict):
        self.altDescription = _dict["altDescription"]
        self.description = _dict["description"]
        self.takeable = _dict["takeable"]
        self.name = _dict["name"]
        self.type = _dict["type"]

    def Encode(self):
        myDict = self.__dict__
        myDict['location'] = None
        return myDict

    def Use(self, _actorUsedWith):
        pass

