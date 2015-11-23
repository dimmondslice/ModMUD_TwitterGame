from Command import Command
from Map import Map

class Go (Command):
    """You use this to go"""
    def __init__(self):
        super(Go, self).__init__()

        self.Grammer = [["go","move", "walk"],["north","south","east","west","poop"]]

    def MovePlayer(self, _player, direction, newroomID):
        print "moving..."
        _player.location.players.remove(_player.name)
        for room in Map.rooms:
            if room.ID == newroomID:
                _player.location = room
                room.players.append(_player.name)
        return "You went " + direction + ". Entered " + str(_player.location.description)

    def Parse(self, _words, _directMessage, _player):
                    #list of strings
        if len(_words) != 2:
            return 'improper use of "go" command. Try: "go" "west"'

        #make sure the direction the enetered was a valid direction
        elif _words[1] in self.Grammer[1]:
            newroomID = _player.location.neighbors[_words[1]]
            print "newroomid: " + str(newroomID)
            if newroomID != "00":
                return self.MovePlayer(_player, _words[1], newroomID)
            else:
                return "You gallantly walk straight into a wall. Nice"
        else:
            return '"' + _words[1] + "\" is not a recognized direction"

