from Player import Player

class Game(object):
	"""docstring for Game"""
				 	   #list of strings
	def __init__(self, _playerIDs):
		super(Game, self).__init__()
		self.running = True
		self.players = {}
		self.CreatePlayers(_playerIDs)
	def Update(self):
		pass
	def CreatePlayers(self, _playerIDs):
		for ID in _playerIDs:
			self.players[ID] = Player(ID)

	def SaveGameState(self):
		pass
	def RunGame(self):
		while g.running:
			#messages = twit.GetMessages()

			#if messages != None:
				#p.Parse(messages[p.name])

			self.Update()
			p.ParseMessage(raw_input("command: "))

