from Command import Command
from TwitterInterface import TwitterInterface

#Command type object that is used to intact with the twitter interface to tweet out a 
#highlight of the recent conversation between the bot and the user
#See Command class for general info on how commands work

class Tweet(Command):
    """docstring for Tweet"""
    def __init__(self):
        super(Tweet, self).__init__()

        self.name = "tweet"
        self.grammer = [["tweet"],[]]
        self.description = "Send the last few lines to a tweet from the bot. 'tweet [number]'."

    #called from the Players ParseMessage(), this is overridden by the other commands
    def Parse(self, words, _dm, _player):
            #words = list of strings that have been tolower()ed
            #_directMessage = [userName, messagetext, messageid,]
            #_player = player type, the player who called this command
        response = ""
        if len(words) == 1:
            self.twit.SendPic(_dm[0], _dm[2])
            response = "You just tweeted the last 4 messages"
        #if message is of the form " tweet 6" tweet the last 6 messages so long as "6" is a number
        elif len(words) == 2:
            #test to ensure that words[1] is an int
            try:
                int(words[1])
            except ValueError:
                self.twit.SendMessage(_dm[2], _dm[1], words[1] + " is not a number", _dm[0])
                return

            response = "You just tweeted the last "+words[1]+ " messages"
            #tweet out a hightlights pictuer that displays the last  words[1] number of messages between the player and the bot
            self.twit.SendPic(_dm[0], _dm[2], int(words[1]))

        #if more then 2 words are entered, send an error
        elif len(words) > 2:
            response = 'Improper use of "tweet" command. Try "Tweet" or "Tweet X" where X is a number'


        #send the response back to the user using direct message
        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])