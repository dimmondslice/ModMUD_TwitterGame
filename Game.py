from Player import Player
from TwitterInterface import TwitterInterface
from Map import *
from Singleton import Singleton
from KeyHalf import KeyHalf

@Singleton
class Game(object):
    """docstring for Game"""
                       #list of strings
    def __init__(self):
        self.running = True
        self.twitFace = TwitterInterface.Instance()
        self.map = Map.Instance()
        self.map.DecodeMap()
        print len(self.map.rooms)
        self.players = {}
        

    #returns a player object with the requested username
    def FindPlayer(self, _username):
        for room in self.map.rooms:
            #print room.name
            for p in room.players:
                #print p.name
                if p.name == _username:
                    print "found player"
                    return True
        return False

    #called in init to instantiate all of the players necesary
    def CreatePlayers(self, _usernames):
        #self.map.DecodeMap()
                            # list of strings
        #loop through room IDs 5-12 aka (0-7)+5 for every player
        roomidItr = 0
        for ID in _usernames:
            currRoomID = (roomidItr % 8) + 5
            if self.FindPlayer(ID) == False:
                self.players[ID] = Player(ID)       #create a player object for every username
                #print "not in map"
                #add the player to the map.
                for room in self.map.rooms:
                    if room.ID == currRoomID:
                        print(str(ID) + " placed in room "  + str(currRoomID))
                        self.players[ID].location = room
                        room.players.append(self.players[ID])
                        roomidItr += 1 #increment room id for next player, if any

                        #by default every character gets a half key in their inventory! 
                        newKeyDict = {
                            "description": "A part of a key. It's the bit on top that you hold it by.", 
                            "name": "CellKey "+ room.name + "BackHalf", 
                            "altDescription": "Two halves make a whole.", 
                            "type": "KeyHalf", 
                            "takeable": True, 
                            "location": None
                        }
                        key = KeyHalf(_dict = newKeyDict)
                        self.players[ID].AddToInventory(key)
                        break
            else:
                #get the reference to the player if it exists already
                for room in self.map.rooms:
                    for p in room.players:
                        if p.name == ID:
                            self.players[ID] = p
                            print str(ID) + " already in map!"
                            """
                            #by default every character gets a half key in their inventory! 
                            newKeyDict = {
                                "description": "A part of a key. It's the bit on top that you hold it by.", 
                                "name": "CellKey "+ room.name[5] + " BackHalf", 
                                "altDescription": "Two halves make a whole.", 
                                "type": "KeyHalf", 
                                "takeable": True, 
                                "location": None,
                                "otherHalf" : "CellKey "+ room.name[5] + " FrontHalf"
                            }
                            key = KeyHalf(_dict = newKeyDict)
                            self.players[ID].AddToInventory(key)
                            print("everyone gets a key!!!!")"""

    #only called once after constructing the Game object, this begins the master while loop
    def RunGame(self):
        #print("started game")
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
    def SaveGame(self):
        self.map.EncodeMap()
