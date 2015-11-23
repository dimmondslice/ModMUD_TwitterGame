from Player import Player
from TwitterInterface import TwitterInterface
from Map import *

class Game(object):
    """docstring for Game"""
    #static dictionary of all players in the form name: player object
    players = {}
                       #list of strings
    def __init__(self, _usernames):
        super(Game, self).__init__()
        self.running = True
        self.twitFace = TwitterInterface.Instance()
        self.map = Map()
        self.map.DecodeJSON()

        self.CreatePlayers(_usernames)


    def FindPlayer(self, username):
        for room in self.map.rooms:
            if room.players != None:
                for p in room.players:
                    if p == username:
                        return True
        return False

    def CreatePlayers(self, _usernames):
                            # list of strings
        for ID in _usernames:
            print(ID)
            players[ID] = Player(ID)       #create a player object for every username
            if self.FindPlayer(ID) == False:
                print "add " + ID + " to map!"
                #add the player to the map
                for room in self.map.rooms:
                    if room.ID == '01':
                        "found room to put him in"
                        players[ID].location = room
                        room.players.append(ID)
                        print "added! room.players is " + str(room.players)
                        break
            else:
                print ID + " already in map!"


    def SaveGameState(self):
        pass

    def Update(self):
        pass

    #only called once after constructing the Game object, this begins the master while loop
    def RunGame(self):
        print("started game")

        while self.running:
            messages = self.twitFace.getMessages()          #grab the messages from the twitter interface
            #each message in form [user:string, text:string, id:int]

            for message in messages:
                #send the message to the player so it can parse it, and choose a command, then return the response to send back to the user
                players[message[0]].ParseMessage(message)
