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
        self.map = Map.Instance()
        self.map.DecodeJSON()
        self.players = {}

    #returns a player object with the requested username
    def FindPlayer(self, username):
        for room in self.map.rooms:
            if room.players != None:
                for p in room.players:
                    if p == username:
                        return True
        return False

    #called in init to instantiate all of the players necesary
    def CreatePlayers(self, _usernames):
                            # list of strings
        #loop through room IDs 5-12 aka (0-7)+5 for every player
        roomidItr = 0
        for ID in _usernames:
            currRoomID = (roomidItr % 8) + 5
            self.players[ID] = Player(ID)       #create a player object for every username
            if self.FindPlayer(ID) == False:
                print "not in map"
                #add the player to the map.
                for room in self.map.rooms:
                    if room.ID == currRoomID:
                        print(str(ID) + " placed in room "  + str(currRoomID))
                        self.players[ID].location = room
                        room.players.append(ID)
                        roomidItr += 1 #increment room id for next player, if any
                        break
            else:
                print str(ID) + " already in map!"

    #only called once after constructing the Game object, this begins the master while loop
    def RunGame(self):
        print("started game")
        Map.Instance().EncodeMap()
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
