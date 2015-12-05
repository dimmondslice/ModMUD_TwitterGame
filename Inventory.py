from Command import Command

#Command type object that will show a player what is currently in their inventory
#See Command class for general info on how commands work

class Inventory(Command):
    """docstring for Inventory"""
    def __init__(self):
        super(Inventory, self).__init__() 

        self.name = "inventory"
        self.grammer = [["inventory"]]

    #called from the Players ParseMessage(), this is overridden by the other commands
    def Parse(self, words, _dm, _player):
            #words = list of strings that have been tolower()ed
            #_directMessage = [userName, messagetext, messageid,]
            #_player = player type, the player who called this command
        if len(words) == 1:      
            response =  _player.PrintInventory() 
        else:
            response = "incorrect usage of inventory command"
        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])