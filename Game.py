from Player import Player
import TwitterInterface

class Game(object):
	"""docstring for Game"""
				 	      #twitter interface  #list of strings
	def __init__(self,    _twitFace,         _usernames):
		super(Game, self).__init__()
		self.running = True
		self.twitFace = _twitFace
		self.players = {}
		self.CreatePlayers(_usernames)
	def Update(self):
		pass
							# list of strings
	def CreatePlayers(self, _usernames):
		for ID in _usernames:
			self.players[ID] = Player(ID)

	def SaveGameState(self):
		pass
	def RunGame(self):
		while self.running:
			messages = twitFace.GetMessages()

			if messages != None:
				for message in messages:
					players[message[0]].ParseMessage(messages[1])

			self.Update()
			#p.ParseMessage(raw_input("command: "))

