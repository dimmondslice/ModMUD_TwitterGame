from Entity import *

class Command(Entity):
    """docstring for Command"""
    def __init__(self):
        super (Command, self).__init__()
        #the grammer is defined as a list of list of strings, each list containing every valid word for that position in the sentence
        self.Grammer = [[]]
        self.twit = TwitterInterface.Instance()
                    
    def Parse(self, words, _directMessage, _player):
                    #list of strings
        return "Yo you should have overloaded Command.Parse()"



        