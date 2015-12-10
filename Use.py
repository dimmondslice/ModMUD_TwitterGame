from Command import Command

class Use(Command):
    """docstring for Use"""
    def __init__(self):
        super(Use, self).__init__()

        self.name = Use
        self.grammer = [["use"],[],["on","with"],[]]
        
    #called from the Players ParseMessage(), this is overridden by the other commands
    def Parse(self, _words, _dm, _player):
            #words = list of strings that have been tolower()ed
            #_dm = [userName, messagetext, messageid,]
            #_player = player type, the player who called this command
        context = _player.GetActorContext()
        self.grammer[1] =  context.keys()
        self.grammer[3] = context.keys()

        response = "Use response"  
        for i in xrange(0,len(self.grammer)):
            for j in xrange(0, len(_words)):
                if(_words[j] not in self.grammer[i]):
                    response = "Incorrect usage of Use command. Make sure the object you're using already exists! Try 'Use' [object] 'on' [object]"

        if(len(_words) != 4):
            response = "Incorrect usage of Use command. Try 'Use' [object] 'on' [object]"
        else:
            response = "You used the " + _words[1] + " on the " + _words[3] + '\n'
            response += context[_words[3]].Use(context[_words[1]])
            print("returned from celldoor use")

        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])


