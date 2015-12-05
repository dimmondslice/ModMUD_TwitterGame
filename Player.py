from Person import Person
from Go import Go
from Tweet import Tweet
from Leave import Leave
from Inventory import Inventory
from TwitterInterface import TwitterInterface
from Map import Map
from Take import Take
from Inspect import Inspect
from Help import Help

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
            "inspect" : Inspect(),
            "help" : Help()
        }
        #dictionary of all actors available to this player including inventory, room contents, etc
        #of the form "name of actor" : actor reference
        self.actorContext = {}
    
    #reads in the direct message from the player, lower() and split() on the string, 
    #then call the appropriate command based on the first word in the message                      
    def ParseMessage(self, _directMessage):
                    #_directMessage = list of strings taken from twitter [username, text of the message, message id]

        words = _directMessage[1].lower().split()

        #loop over ever word in words, if that word is not in the actor context, see if that word and the next are meant to refer 1 actor
        #if you find an actor whose name is words[i] + words[i+1] then adjust words[] to reflect the actor names, rather than individual words
        context = self.GetActorContext()
        i = 1    #counter var, start at one because don't need to worry about the command being more than one word long, for now at least
        while i < len(words) -1:       #start at the second word and don't check the last word
            print(i)    
            if words[i] not in context.keys():
                #if the second word is not in the actor contex, search in the context through every actor
                for actorName in context.keys():
                    #if the actor name contains this word, perhaps this word and the next are referring to this actor
                    if words[i] in actorName:
                        if words[i] + " " + words[i+1] == actorName.lower():
                            words[i] = words[i] + " " + words[i+1]
                            del(words[i+1])
            i+=1

        #now actually send the command
        if words[0] in self.verbContext:
            self.verbContext[words[0]].Parse(words, _directMessage, self)
        else:
            #tell the player that they didn't enter a valid command
            TwitterInterface.Instance().sendMessage(_directMessage[2], _directMessage[1] ,words[0] + " is not a recognized command", _directMessage[0])


    #returns a dictionary of all the actors in this players inventory and all the actors in their current room location
    #return in the form {string actorName : Actor act}
    def GetActorContext(self, includeInventory = True, includeRoom = True):
        context = {}
        #populate the context with the items in your inventory
        if(includeInventory):
            for item in self.inventory:
                context[item.name.lower()] = item
        if(includeRoom):
            for actor in self.location.actors:
                context[actor.name.lower()] = actor

        return context
        