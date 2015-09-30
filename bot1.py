#basic framework for call and response twitterbot.
#finds tweets that @mention the bot and save them into a "queue"
#takes a tweet off the queue and replies to 1 every two minutes, to avoid rate limiting.
#if closed, and reopened later, able to know which @mentions it has and hasn't replied to yet, so it can pick up where it left off without missing any commands
#will pick up where it left off when code execution is stopped and resumed, but not if disconnects/reconnects to internet while running. needs to be implemented!

#currently stores small amount of info in a text file. Eventually that info, along with player progress, should be stored in an SQL database.

import tweepy
import json
import Queue
import time


#   NOTE: IF YOU WANT TO TEST AND RUN THIS CODE YOURSELF, CREATE A NEW TWITTER ACCOUNT AND CHANGE THE
#   CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET, AND BOTNAME VARIABLES!!
#   this is bc the info in last.txt is important to avoid duplicate replies, so running it on your own will cause it to reply to the same tweet twice,
#   and get punished for duplicate tweets!
CONSUMER_KEY = 'SNgHvKkkYwxpGZcJiKTwPfDbv'
CONSUMER_SECRET = 'qaFXmZVZytrZrNeu3y0P5Fprx9sWQY66cjzjEMm3NjRozydlJI'
ACCESS_KEY = '3745260316-YbIuTAoAZrCf5nWxrlGLtiib2L2oClGNSMxJS3x'
ACCESS_SECRET = 'twnynteVz0XRBNlZjE6w69RxYllVTfe6sKXPBR2hAX6dL'
BOTNAME = 'SDADtemp'


#should be its  own file
class Command:
    user = ""
    action = ""
    id = 0

    def __init__(self, u, a, i):
        self.user = u
        self.action = a.replace("@" + BOTNAME + " ", "")
        self.id = i


#should be its  own file
def generateResponse(command):
    #for now, just tweet back to them the message they sent you
    return "@" + command.user + " " + command.action



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

commands = [] # treat as FIFO queue, add at end, remove at beginning.
while True:
    print "LOOP"
    #find all tweets containing the botname, to find @mentions of bot.
    try:
        tweets = api.search(q=BOTNAME, since_id=last_id)
        for tweet in reversed(tweets):
            if last_id < int(tweet.id) :
                last_id = int(tweet.id)
            mentions =  tweet.entities["user_mentions"]
            for mention in mentions:
                if mention["screen_name"] == BOTNAME:
                    print "ADDED: " + tweet.text
                    print tweet.id
                    command = Command(tweet.user.screen_name, tweet.text, tweet.id)
                    commands.append(command)

    except tweepy.TweepError as e:
        print "error: " + e
        # depending on TweepError.code, one may want to retry or wait

    print "a"

    if len(commands) > 0:
        print "not empty"
        command = commands[0]
        del commands[0]
        print"pop"
        response = generateResponse(command)
        api.update_status(status=response)
        print('POSTED: ' + response)

        #save last processed command
        print command.id
        f = open("last.txt", "w")
        f.write(str(command.id))
        f.close()
    else:
        print "queue empty, nothing to post"

    time.sleep(120)