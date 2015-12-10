from Command import Command
from KeyHalf import KeyHalf
from Actor import Actor

class Combine(Command):
    """docstring for Combine"""
    def __init__(self):
        super(Combine, self).__init__()
        
        self.name = "combine"
        self.grammer = [["combine"],[],["with", "and"],[]]
    
    def CombineThem():
        pass
    #called from the Players ParseMessage(), this is overridden by the other commands
    def Parse(self, _words, _dm, _player):
            #words = list of strings that have been tolower()ed
            #_dm = [userName, messagetext, messageid,]
            #_player = player type, the player who called this command
        context = _player.GetActorContext()
        self.grammer[1] =  context.keys()
        self.grammer[3] =  self.grammer[1]

        response = "combine response"

        if(len(_words) != 4):
            response = "incorrect usage of combine"
        if _words[1] in self.grammer[1]:
            key = context[_words[1]]
            if(type(key) is KeyHalf):
                if(type(key) is KeyHalf and key.otherHalf == context[_words[3]].name):
                    #combine them
                    newKeyDict = {
                    "name" : "Cell " + key.name.split()[1] + " Key",
                    "altDescription" : "Use this to unlock the cell door, What did you think it would do?",
                    "takeable" : True,
                    "description" : "Hey look, it's a whole key now!",
                    "type" : "Actor"
                    }
                    newKey = Actor(newKeyDict)
                    _player.AddToInventory(newKey)

                    if(key in _player.inventory):   #if the first key half was in the players inventory
                        _player.inventory.remove(key)
                    else:
                        _player.location.remove(key)    #otherwise remove it from the room

                    if(context[_words[3]] in _player.inventory):   #if the second key half was in the players inventory
                        _player.inventory.remove(context[_words[3]])
                    else:
                        _player.location.remove(context[_words[3]])    #otherwise remove it from the room

            else:
                response = "You can't combine " + _words[1] +" and " + _words[3]
        else:
            response = "can't find " + _words[1]

        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])
            