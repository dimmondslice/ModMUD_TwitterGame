from Player import Player

class Game(object):
	"""docstring for Game"""
	def __init__(self):
		super(Game, self).__init__()
		self.running = True
	def Update(self):
		pass
	def createPlayers():
		pass

g = Game()
p = Player()

while g.running:
	g.Update()
	p.ParseMessage(raw_input("command: "))