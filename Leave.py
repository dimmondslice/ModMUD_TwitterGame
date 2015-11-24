from Command import Command
import Game

class Leave (Command):
    """You use this to go"""
    def __init__(self):
        super(Leave, self).__init__()

        self.grammer = [["leave"],["game"]]

    #called from the Players ParseMessage(), this is overridden by the other commands
    def Parse(self, words, _directMessage, _player):
            #words = list of strings that have been tolower()ed
            #_directMessage = [userName, messagetext, messageid,]
            #_player = player type, the player who called this command
        response = "response"
        
        if len(_words) != 2 or _words[1] not in self.grammer[1]:
            response = 'improper use of "leave" command. Correct use is: "leave game"'

        else:
            #remove player from the game
            _player.location.players.remove(_player.name)
            del Game.Game.Instance().players[_player.name]

            response = "Be Gone!"

        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])

