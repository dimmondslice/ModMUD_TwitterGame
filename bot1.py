#basic framework for call and response twitterbot.
#will pick up where it left off when code execution is stopped and resumed, and if disconnects/reconnects to internet while running

#todo:
#currently stores info in text file. Should eventually update to an SQL database.
#correctly handle different errors from twitter.
#botname, as well as access_key and access_secret, should not be hardcoded! i think consumerkey and consumersecret can be the same app-wide

import tweepy
import json
import Queue
import time


#	IF YOU WANT TO TEST AND RUN THIS CODE YOURSELF, CREATE A NEW TWITTER ACCOUNT AND CHANGE THE
#	CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET, AND BOTNAME VARIABLES!!
CONSUMER_KEY = '6wdteAprvKNdBVC7ttiuiIKDZ'
CONSUMER_SECRET = 'wWeuAgcFwxBPrJoHskpnaIOA7OPpDJjnvoig1TWFJRkP0Zr2Ae'
ACCESS_KEY = '3959461929-7tY4fAomlOncSlusApNXCxZRKSpwGUzh2QZotXg'
ACCESS_SECRET = 'b2QLZKGnwXwYO5M9fPyOlzOKP3ygqlwMpfO9myCwu1ip5'
BOTNAME = 'SDADBOT'
tempFile = open("tempFile.txt",'w')
stopCMD = "Bot Stop"
controlLoop = True


#should be its	own file
class Command:
	user = ""
	action = ""
	id = 0

	def __init__(self, u, a, i):
		self.user = u 										#person who sent it
		self.action = a.replace("@" + BOTNAME + " ", "")	# core of the txt
		self.id = i


#should be its	own file
def generateResponse(command):
	#for now, just tweet back to them the message they sent you
	print "The command action is " + command.action
	if command.action == "Stop":
		controlLoop = False
	return command.action


#connect to twitter streaming api
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

last_id = -1
try:
	f = open("last.txt", "r")
	s = f.readline()
	if s.isdigit() == True:
		last_id = int(s)
	f.close()
except IOError as e:
	print "last.txt not found"

commands = [] # treat as FIFO queue, add at end, remove at beginning. (pythons built in queue class is CRAP)
while controlLoop:
	print "LOOP"
	#find all tweets containing the botname, to find @mentions of bot.
	try:
		#tweets = api.search(q=BOTNAME, since_id=last_id)
		tweets = api.direct_messages(since_id = last_id)
		for tweet in reversed(tweets):
			#print tweet
			if last_id < int(tweet.id) :
				last_id = int(tweet.id)
			'''mentions =	tweet.entities["user_mentions"]
			for mention in mentions:
				if mention["screen_name"] == BOTNAME:
					print "ADDED: " + tweet.text
					if tweet.text == stopCMD:
						print "I got a stop command"
					print tweet.id
					command = Command(tweet.user.screen_name, tweet.text, tweet.id)
					commands.append(command)'''
			command = Command(tweet.user.screen_name, tweet.text, tweet.id)
			commands.append(command)
	except tweepy.TweepError as e:
		print "Error getting commands: " + str(e.reason)
		# depending on TweepError.code, one may want to retry or wait

	if len(commands) > 0:
		print "not empty"
		command = commands[0]
		response = generateResponse(command)
		 #save last processed command
		print command.id
		
		try:
			api.send_direct_message(command.user,text=response)
			del commands[0] #remove command from queue. happens after posting, so if there is an error it stays in the
			print('POSTED: ' + response)
			f = open("last.txt", "w")
			f.write(str(command.id))
			f.close()

		   
		except tweepy.TweepError as e:
			print "Error trying to post status: " + str(e.reason)
			time.sleep(10) #add additional wait to total 20 min in case of error, to avoid too many errors.
			#this will be improved upon in future to better handle specific errors.

	else:
		print "queue empty, nothing to post"

	time.sleep(20)