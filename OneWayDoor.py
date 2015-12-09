from Actor import Actor

class CellDoor(Actor):
	"""docstring for CellDoor"""
	def __init__(self, _dict = None):
		if _dict != None:
            self.Decode(_dict)
        else:
			super(CellDoor, self).__init__()
			self.name = "unnamed cell door"
			self.adjacentRoom = None

	#cell door's use function will unlock the door if the player uses the right key on it, then it will reinstate the connection between the room
	#that contains this door, and the adjacent room
	def Use(self, _actorUsedWith):
		if(_actorUsedWith.name == "cell " + self.location.ID + " key")
	def Decode(self, _dict):
		super(CellDoor, self).Decode(self, _dict)

		#now is when I will actually set self.adjecentRoom, bc I can garauntee I know self.location now

		roomID = self.location.neighbors[ _dict["adjecentRoom"]]
		#within the code,unlike the JSON, self.adjacentRoom is actually a list in the form ["direction this door leads to", id of that room]
		self.adjacentRoom = [ _dict["adjacentRoom"], roomID]
		self.location.neighbors[_dict["adjacentRoom"]] = 0	#have this neighbor point to nothing

		neighborId = self.location.neighbors[_dict["adjacentRoom"]]
		
		
