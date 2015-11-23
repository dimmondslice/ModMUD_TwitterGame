from Person import *
from Go import Go
from Tweet import Tweet
from Leave import Leave
from Inventory import Inventory
from TwitterInterface import TwitterInterface

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
            "leave" : Leave()
        }

    def ParseMessage(self, _directMessage):
                           #list of strings taken from twitter [username, text of the message, message id]
        words = _directMessage[1].lower().split()
        if words[0] in self.verbContext:
            self.verbContext[words[0]].Parse(words, _directMessage, self)
        else:
            print words[0] + " is not a recognized command"

