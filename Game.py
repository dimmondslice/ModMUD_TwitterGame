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
        self.players = {}
		
        self.CreatePlayers(_usernames)


    def FindPlayer(self, username):
        for room in self.map.rooms:
            if room.players != None:
                for p in room.players:
                    if p == ID:
                        return True
        return False

    def CreatePlayers(self, _usernames):
                            # list of strings
        for ID in _usernames:
            print(ID)
            self.players[ID] = Player(ID)       #create a player object for every username
            if self.FindPlayer(ID) == False:
                #add the player to the map
                for room in self.map.rooms:
                    if room.ID == '01':
                        if room.players == None:
                            room.players == [ID]
                        else:
                            room.players.append(ID)
                        break


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
                self.players[message[0]].ParseMessage(message)

                #response = self.players[message[0]].ParseMessage(message[1])
                #self.twitFace.SendMessage(message[2],message[1],response,message[0])
                #temporary direct parsing for the tweet command to test functionality

                if message[1].lower() == "tweet":
                    self.twitFace.SendPic(message[0], message[2])                    
                #if message[1].lower() == "inventory":
                    #self.players[message[0]].PrintInventory()
                    #print("game-inventory parse")
