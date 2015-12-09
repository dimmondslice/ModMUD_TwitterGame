from Combine import Combine

class Combine(Command):
	"""docstring for Combine"""
	def __init__(self):
		super(Combine, self).__init__()
		
		self.name = "combine"
		self.grammer = [["combine"],[],["with"],[]]
		
	#called from the Players ParseMessage(), this is overridden by the other commands
    def Parse(self, _words, _dm, _player):
            #words = list of strings that have been tolower()ed
            #_dm = [userName, messagetext, messageid,]
            #_player = player type, the player who called this command
        response = "response"
