from Player import Player

class Game(object):
	"""docstring for Game"""
	def __init__(self):
		super(Game, self).__init__()
		self.running = True
	def Update(self):
		pass
	def CreatePlayers():
		pass
	def SaveGameState():
		pass

g = Game()
p = Player()

#twit = TwitterInterface()

while g.running:

	#messages = twit.GetMessages()

	#if messages != None:
		#p.Parse(messages[p.name])

	g.Update()
	p.ParseMessage(raw_input("command: "))