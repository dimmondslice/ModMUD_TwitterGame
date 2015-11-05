from Command import Command
from TwitterInterface import TwitterInterface

class Tweet(Command):
    """docstring for Tweet"""
    def __init__(self):
        super(Tweet, self).__init__()
    def Parse(self, words):
        #TwitterInterface.ref.sendPic("actuallyspenc", )
        return "Tweeted."
        #if len(words) != 2:
            #return 'Improper use of "tweet" command.'
        #else:
            #return "You just tweeted the last 3 messages"
        #put the tweeting and pil stuff here
        