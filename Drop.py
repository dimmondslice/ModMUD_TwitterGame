from Command import Command

class Drop(Command):
    """docstring for Drop"""
    def __init__(self):
        super(Drop, self).__init__()
        
        self.name = "drop"
        self.grammer = [["drop"],[]]
        self.description = "Drop an item from your inventory into the room. 'drop [item name]'."

     #called from the Players ParseMessage(), this is overridden by the other commands
    def Parse(self, _words, _dm, _player):
            #words = list of strings that have been tolower()ed
            #_dm = [userName, messagetext, messageid,]
            #_player = player type, the player who called this command
        response = "response"
        if len(_words) != 2:
            response = 'improper use of "drop" command. Try: "drop" [object in your invenotry]'

        else:
            context = _player.GetActorContext(includeInventory = True, includeRoom = False)
            self.grammer[1] = context.keys()

            #if the input word is in the current actor context
            if _words[1] in self.grammer[1]:
                actor = context[_words[1]]
                _player.location.AddActor(actor)

                response = "you dropped " + _words[1]
            else:
                response = "You don't have a " + words[1] + " in your inventory"

        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])

