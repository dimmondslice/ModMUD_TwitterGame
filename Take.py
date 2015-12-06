from Command import Command

#Command type object that allows a player to take an actor from the room they are in and put that actor in their inventory
#See Command class for general info on how commands work

class Take(Command):
    """docstring for Take"""
    def __init__(self):
        super(Take, self).__init__()

        self.name= "take"
        self.grammer = [["take"],[]]

    #called from the Players ParseMessage(), this is overridden by the other commands
    def Parse(self, _words, _dm, _player):
            #words = list of strings that have been tolower()ed
            #_directMessage = [userName, messagetext, messageid,]
            #_player = player type, the player who called this command
        response = "response"
        if len(_words) != 2:      
            response = "incorrect usage of take command"
        else:
            #build actor context for items available to pickup, only add items located in the room you are in, not the players inventory
            #adding this to the grammer is unnecesary but just reinforcing good practice.
            context = {}
            for actor in _player.location.actors:
                context[actor.name] = actor
            self.grammer[1] = context.keys()

            #if the input word is in the current actor context and it can be picked up, then add it to the plaeyrs inventory
            if _words[1] in self.grammer[1]:
                actor = context[_words[1]]
                if actor.takeable == True:
                    _player.AddToInventory(actor)
                    actor.location.RemoveActor(actor)
                    actor.location = None
                    response = "You put the " + _words[1] + " in your inventory"
                else:
                    response = "You can't take the " + _words[1]
            else:
                response = "There is no " + _words[1] + " to take"

        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])
