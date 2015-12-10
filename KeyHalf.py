from Actor import Actor

class KeyHalf(Actor):
    """docstring for KeyHalf"""
    def __init__(self, _dict = None):
        if _dict != None:
            self.Decode(_dict)
        else:
            super(KeyHalf, self).__init__(_dict)
            self.name ="default key name"

        """self.otherHalf = ""
        if("Front" in self.name):
            self.otherHalf = self.name.replace("Front", "Back")
        elif("Back" in self.name):
            self.otherHalf = self.name.replace("Back", "Front")"""
    def Decode(self, _dict):
        super(KeyHalf, self).Decode(_dict)
        self.otherHalf = _dict["otherHalf"]
