from Command import Command

class Go (Command):
    """You use this to go"""
    def __init__(self):
        super(Go, self).__init__()
                    
        self.Grammer = [["go","move", "walk"],["north","south","east","west","poop"]]
    def Parse(self, words):
                    #list of strings
        if len(words) != 2:
            return 'improper use of "go" command. Try: "go" "west"'
        
        #make sure the direction the enetered was a valid direction
        elif words[1] in self.Grammer[1]:
            return "You went " + words[1]
        else:
            return '"' + words[1] + "\" is not a recognized direction"

