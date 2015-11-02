from Command import Command

class Tweet(Command):
	"""docstring for Tweet"""
	def __init__(self):
		super(Tweet, self).__init__()
	def Parse(self, words):
		if len(words) != 2:
			print('Improper use of "tweet" command.')
		else:
			print("You just tweeted the last " + words[1] + " messages")
		#put the tweeting and pil stuff here
		