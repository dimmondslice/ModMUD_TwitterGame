from Command import Command
from TwitterInterface import TwitterInterface

class Tweet(Command):
    """docstring for Tweet"""
    def __init__(self):
        super(Tweet, self).__init__()
    def Parse(self, words):
        return "I've tweeted the last 4 messages."

        
        #if len(words) != 2:
            #return 'Improper use of "tweet" command.'
        #else:
            #return "You just tweeted the last 3 messages"
        #put the tweeting and pil stuff here
        