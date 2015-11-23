from Command import Command
from Game import Game

class Leave (Command):
    """You use this to go"""
    def __init__(self):
        super(Leave, self).__init__()

        self.Grammer = [["leave"],["game"]]

    def Parse(self, _words, _dm, _player):
                    #list of strings
        response = "response"
        if len(_words) != 2 or _words[1] not in self.Grammer[1]:
            response = 'improper use of "leave" command. Correct use is: "leave game"'

        #remove player from the game
        _player.location.players.remove(_player.name)
        del Game.players[_player.name]

        response = "Be Gone!"

        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])

