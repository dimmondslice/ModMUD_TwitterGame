from Actor import *
from Item import Item

class Person(Actor):
    """docstring for Person"""
    def __init__(self):
        super(Person, self).__init__()
        self.inventory = []
        self.InventoryInit()
        self.level = 0
        self.stats = None
        self.gear = None
        self.weapon = None
    #just used to put a couple items in the persons inventory
    def InventoryInit(self):
        pass
    def PrintInventory(self):
        response = "Stuff in your inventory:\n" 
        for i in self.inventory:
            response += "        " + i.name + '\n '
        return response
    def AddToInventory(self, _actor):
        self.inventory.append(_actor)
    def Decode(self, _dict):
       # print _dict
        super(Person,self).Decode(_dict)
       # print _dict["stats"]
        inv = []
        
        self.stats = _dict["stats"]
        self.level = _dict["level"]
        self.weapon = _dict["weapon"]
        self.gear = _dict["gear"]
        
        for item in _dict["inventory"]:
            dummy = Actor(item)
            inv.append(dummy)
            

        self.inventory = inv