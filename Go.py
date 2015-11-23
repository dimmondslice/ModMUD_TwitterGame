from Command import Command
from Map import Map

class Go (Command):
    """You use this to go"""
    def __init__(self):
        super(Go, self).__init__()

        self.grammer = [["go","move", "walk"],["north","south","east","west"]]

    def MovePlayer(self, _player, direction, newroomID):
        print "moving..."
        _player.location.players.remove(_player.name)
        for room in Map.rooms:
            if room.ID == newroomID:
                _player.location = room
                room.players.append(_player.name)
        return "You went " + direction + ". Entered " + str(_player.location.name)

    def Parse(self, _words, _dm, _player):
                    #list of strings
        response = "response"
        if len(_words) != 2:
            response = 'improper use of "go" command. Try: "go" "west"'

        #make sure the direction the enetered was a valid direction
        elif _words[1] in self.grammer[1]:
            newroomID = _player.location.neighbors[_words[1]]
            print "newroomid: " + str(newroomID)
            if newroomID != "00":
                response = self.MovePlayer(_player, _words[1], newroomID)
            else:
                response = "You gallantly walk straight into a wall. Hopefully no one saw that"
        else:
            response = '"' + _words[1] + "\" is not a recognized direction"

        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])

