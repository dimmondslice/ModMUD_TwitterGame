#basic call/response core

#todo:
#currently stores info in text file. Should eventually update to a database.
#correctly handle different errors from twitter.
#botname, as well as access_key and access_secret, should not be hardcoded! i think consumerkey and consumersecret should be the same app-wide
#Currently I am saving a local copy of the image before i post it. In documentation it looks like you should be able to send it without saving the file first. look into it.

import tweepy
import time
import Img


#	IF YOU WANT TO TEST AND RUN THIS CODE YOURSELF, CREATE A NEW TWITTER ACCOUNT AND CHANGE THE
#	CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET, AND BOTNAME VARIABLES!!
CONSUMER_KEY = '6wdteAprvKNdBVC7ttiuiIKDZ'
CONSUMER_SECRET = 'wWeuAgcFwxBPrJoHskpnaIOA7OPpDJjnvoig1TWFJRkP0Zr2Ae'
ACCESS_KEY = '3959461929-7tY4fAomlOncSlusApNXCxZRKSpwGUzh2QZotXg'
ACCESS_SECRET = 'b2QLZKGnwXwYO5M9fPyOlzOKP3ygqlwMpfO9myCwu1ip5'
BOTNAME = 'SDADBOT'

stopCMD = "Stop"
postPicture = "Print"
log = dict()
last_id = -1 #initial assignment, in case running for the first time.
commands = [] # treat as FIFO queue, add at end, remove at beginning. (pythons built in queue class is CRAP)


class Command:
    user = ""
    action = ""
    id = 0

    def __init__(self, u, a, i):
        self.user = u 										# person who sent it
        self.action = a.replace("@" + BOTNAME + " ", "")	# core of the txt
        self.id = i                                         # message id number


def generateResponse(command):
    #for now, just tweet back to them the message they sent you
    print "The command action is: " + command.action

    return command.action


def SendPic(command):
    global commands
    messagelist = []
    if command.user in log:
        userhist = log[command.user]
        messagelist.append(userhist[-2][1])
        messagelist.append(userhist[-1][0])
        messagelist.append(userhist[-1][1])
    else:
        messagelist.append("Play the game first!!!")

    image = Img.gen(messagelist)

    try:
        image.save("123.png")
    except IOError:
        print("cannot convert")

    try:
        api.update_with_media(filename = "123.png", status = "Here is a highlight from @" + command.user)
        del commands[0] #remove command from queue. happens after posting, so if there is an error it stays in
        print('POSTED pic to ' + command.user)
        f = open("last.txt", "w")
        f.write(str(command.id))
        f.close()

        #do not update the log when posting a highlight. only keeps track of actual game commands.

    except tweepy.TweepError as e:
        print "Error trying to post status: " + str(e.reason)
        time.sleep(60) #add additional wait of 1 min in case of error, to avoid too many errors.
		#this will be improved upon in future to better handle specific errors.

def SendDM(command,response):
    global commands
    global log

    print command.id

    try:
        api.send_direct_message(command.user,text=response)
        del commands[0] #remove command from queue. happens after posting, so if there is an error it stays in
        print('POSTED: ' + response)
        f = open("last.txt", "w")
        f.write(str(command.id))
        f.close()

        print "Log before: " + str(log)
        if command.user in log:
            log[command.user].append([command.action, response])
        else:
            log[command.user] =  [[command.action, response]]
        print "Log after: " + str(log)

    except tweepy.TweepError as e:
        print "Error trying to post status: " + str(e.reason)
        time.sleep(60) #add additional wait of 1 min in case of error, to avoid too many errors.
		#this will be improved upon in future to better handle specific errors.


def ReadDM():
    global commands
    global last_id
    try:
        print "LASTID:: " + str(last_id)
        tweets = api.direct_messages(since_id = last_id)
        for tweet in reversed(tweets):
            if last_id < int(tweet.id) :
                last_id = int(tweet.id)
            if tweet.text == stopCMD :
                print "I got a stop command"
            command = Command(tweet.sender.screen_name, tweet.text, tweet.id)
            commands.append(command)
    except tweepy.TweepError as e:
        print "Error getting commands: " + str(e.reason)
        # depending on TweepError.code, one may want to retry or wait

def ReadTweets():
    global commands
    global last_id
    try:
        tweets = api.search(q=BOTNAME, since_id=last_id)
        for tweet in reversed(tweets):
            if last_id < int(tweet.id) :
                last_id = int(tweet.id)
            mentions =	tweet.entities["user_mentions"]
            for mention in mentions:
                if mention["screen_name"] == BOTNAME:
                    print "ADDED: " + tweet.text
                    if tweet.text == stopCMD:
                        print "I got a stop command"
                    print tweet.id
                    command = Command(tweet.user.screen_name, tweet.text, tweet.id)
                    commands.append(command)
    except tweepy.TweepError as e:
        print "Error getting commands: " + str(e.reason)
        # depending on TweepError.code, one may want to retry or wait




#connect to twitter streaming api
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

try:
	f = open("last.txt", "r")
	s = f.readline()
	if s.isdigit() == True:
		last_id = int(s)
	f.close()
except IOError as e:
	print "last.txt not found"

while True:
    print "LOOP"

    #Read in messages - currently only reading direct messages. May end up needing both.
    ReadDM()
    #ReadTweets()

    #post message
    if len(commands) > 0:
        print "not empty"
        command = commands[0]
        if command.action == postPicture:
            SendPic(command)
        elif command.action == stopCMD :
            del commands[0]
            break
        else:
            response = generateResponse(command)
            SendDM(command,response)

    else:
        print "queue empty, nothing to post"

    time.sleep(60)