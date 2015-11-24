from Entity import *

#this class will be overwritten by other command type ojects,and will handle all of the logic that any given command does, 
#as well as outputs the commands response the twitter use that called it

class Command(Entity):
    """Abstract class to be inherited by actual commands"""
    def __init__(self):
        super (Command, self).__init__()
        #the grammer is defined as a list of list of strings, each list containing every valid word for that position in the sentence
        self.grammer = [[]]

        #reference to the twitter interface singleton for all other commands to use
        self.twit = TwitterInterface.Instance()

    #called from the Players ParseMessage(), this is overridden by the other commands
    def Parse(self, words, _directMessage, _player):
            #words = list of strings that have been tolower()ed
            #_directMessage = [userName, messagetext, messageid,]
            #_player = player type, the player who called this command
        return "Yo you should have overloaded Command.Parse()"

    #this will be used to update a commands grammer to reflect the players environment
    def ContextualizeGrammer():
    	pass



        