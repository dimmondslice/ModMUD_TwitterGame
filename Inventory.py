from Command import Command

class Inventory(Command):
    """docstring for Inventory"""
    def __init__(self):
        super(Inventory, self).__init__()       
        self.grammer = [["inventory"]]

    def Parse(self, _words, _dm, _player):
        if len(_words) == 1:      
            response =  _player.PrintInventory() 
        else:
            response = "incorrect usage of inventory command"
        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])