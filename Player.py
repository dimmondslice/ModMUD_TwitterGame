from Person import *
from Go import Go
from Tweet import Tweet
from Leave import Leave
from Inventory import Inventory
from TwitterInterface import TwitterInterface
from Map import Map
from Take import Take
from Inspect import Inspect

class Player(Person):
    """docstring for Player"""
    def __init__(self, _username):
        super(Player, self).__init__()
        self.name = _username

        #the list of all command objects this player has access to at the moment
        self.verbContext = {
            "go" : Go(),
            "tweet" : Tweet(),
            "inventory" : Inventory(),
            "take" : Take(),
            "leave" : Leave(),
            "inspect" : Inspect()
        }
        #dictionary of all actors available to this player including inventory, room contents, etc
        #of the form "name of actor" : actor reference
        self.actorContext = {}
    
    #reads in the direct message from the player, lower() and split() on the string, 
    #then call the appropriate command based on the first word in the message                      
    def ParseMessage(self, _directMessage):
                    #_directMessage = list of strings taken from twitter [username, text of the message, message id]

        words = _directMessage[1].lower().split()
        if words[0] in self.verbContext:
            self.verbContext[words[0]].Parse(words, _directMessage, self)
        else:
            print words[0] + " is not a recognized command"

    #returns a dictionary of all the actors in this players inventory and all the actors in their current room location
    #return in the form {string actorName : Actor act}
    def GetActorContext(self):
        context = {}
        #populate the context with the items in your inventory
        for item in self.inventory:
            context[item.name] = item
        for actor in self.location.actors:
            context[actor.name] = actor

        return context




