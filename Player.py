from Person import *
from Go import Go
from Tweet import Tweet

class Player(Person):
    """docstring for Player"""
    def __init__(self, _username):
        super(Player, self).__init__()
        self.name = _username

        #the list of all command objects this player has access to at the moment
        self.verbContext = {
            "go" : Go(),
            "tweet" : Tweet()
        }

                            
    def ParseMessage(self, message):
                           #input string
        words = message.lower().split()
        if words[0] in self.verbContext:
            return self.verbContext[words[0]].Parse(words)
        else:
            return words[0] + " is not a recognized command"

