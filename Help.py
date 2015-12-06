from Command import Command


class Help(Command):
    """docstring for Help"""
    def __init__(self):
        super(Help, self).__init__()

        self.grammer = [["help"],[]]
        self.name = "help"
        self.description = "Do you really need help with the help command? Try typing 'help [command]'"

    def Parse(self, _words, _dm, _player):
            #words = list of strings that have been lower()ed
            #_dm = [userName, messagetext, messageid,]
            #_player = player type, the player who called this command
        response = "response"

        #if the don't ask for help with a specific command
        if(len(_words) == 1):
            response = "You can interact with things using commands. Here is the full list of commands available to you right now " \
                        + "(for more info about any of the commands try typing 'help [command]'' )\n"
    
            for comm in _player.verbContext.values():
                response +="        " + comm.name + "\n"

        #get the help text for a specific command
        elif(_words[1] in _player.verbContext.keys()):
            response = _player.verbContext[_words[1]].description
        else:
            response = _words[1] + " is not recognized"

        #send the response to the player via direct message
        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])