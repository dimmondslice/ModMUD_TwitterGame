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
			print(ID)
			self.players[ID] = Player(ID)

	def SaveGameState(self):
		pass
	def RunGame(self):
		print("started game")
		while self.running:
			messages = self.twitFace.getMessages()

			if messages != []:
				for message in messages:
					self.players[message[0]].ParseMessage(message[1])
					if message[2].islower() == "tweet":
						twitFace.SendPic(message[0], message[2])

			self.Update()
			#p.ParseMessage(raw_input("command: "))

