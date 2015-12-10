from Command import Command
from Map import Map

#command type object that moves a player to one of the adject rooms on the map based on their imput
#See Command class for general info on how commands work

class Go (Command):
    """You use this to go"""
    def __init__(self):
        super(Go, self).__init__()

        self.name = "go"
        self.grammer = [["go","move", "walk"],["north","south","east","west"]]
        self.description = "Move to a new room in one of the cardinal directions. 'go west', 'go east', 'go north', or 'go south'."

    #used in this class to move the players location based on their input
    def MovePlayer(self, _player, direction, newroomID):
        print "moving..."
        _player.location.players.remove(_player)
        for room in Map.Instance().rooms:
            if room.ID == newroomID:
                _player.location = room
                room.players.append(_player)
        return "You went " + direction + ". Entered " + str(_player.location.name)

    #called from the Players ParseMessage(), this is overridden by the other commands
    def Parse(self, _words, _dm, _player):
            #words = list of strings that have been tolower()ed
            #_dm = [userName, messagetext, messageid,]
            #_player = player type, the player who called this command
        response = "response"
        if len(_words) != 2:
            response = 'improper use of "go" command. Try: "go" "west"'

        #make sure the direction the enetered was a valid direction
        elif _words[1] in self.grammer[1]:
            newroomID = _player.location.neighbors[_words[1]]
            print "newroomid: " + str(newroomID)
            if newroomID != 0:
                response = self.MovePlayer(_player, _words[1], newroomID)
            else:
                response = "You gallantly walk straight into a wall. Hopefully no one saw that"
        else:
            response = '"' + _words[1] + "\" is not a recognized direction"

        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])

