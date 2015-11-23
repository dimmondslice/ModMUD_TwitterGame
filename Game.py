from Player import Player
from TwitterInterface import TwitterInterface
from Map import *
from Singleton import Singleton

@Singleton
class Game(object):
    """docstring for Game"""
                       #list of strings
    def __init__(self):
        self.running = True
        self.twitFace = TwitterInterface.Instance()
        self.map = Map()
        self.map.DecodeJSON()
        self.players = {}

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
            self.players[ID] = Player(ID)       #create a player object for every username
            if self.FindPlayer(ID) == False:
                print "add " + ID + " to map!"
                #add the player to the map
                for room in self.map.rooms:
                    if room.ID == '01':
                        "found room to put him in"
                        self.players[ID].location = room
                        room.players.append(ID)
                        #print "added! room.players is " + str(room.players)
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
                try:
                    self.players[message[0]].ParseMessage(message)
                except KeyError:
                    #twitter user is not a player in the game
                    print message[0] + " is not a player. message ignored"
