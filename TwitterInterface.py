import tweepy
import time
import Img
import sqlite3

class TwitterInterface(object):
    CONSUMER_KEY = '6wdteAprvKNdBVC7ttiuiIKDZ'
    CONSUMER_SECRET = 'wWeuAgcFwxBPrJoHskpnaIOA7OPpDJjnvoig1TWFJRkP0Zr2Ae'
    READWAITTIME = 60
    POSTWAITTIME = 5
    PICWAITTIME = 5 #todo: unsure if its actually 5! must test!


    def __init__(
                self,
                aKey = '3959461929-7tY4fAomlOncSlusApNXCxZRKSpwGUzh2QZotXg',
                aSecret = 'b2QLZKGnwXwYO5M9fPyOlzOKP3ygqlwMpfO9myCwu1ip5',
                botName = 'SDADBOT'):
        '''set self.api,self.lastRead,self.timerRead,self.timerPost,self.botName
        key,secret,botname passed in to eventually support alt accounts'''
        self.timerRead = 0
        self.timerPost = 0
        self.timerPic = 0
        self.botName = botName

        try:
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(aKey, aSecret)
            self.api = tweepy.API(auth)
        except Exception as e:
            #invalid credentials! todo: should raise an error
            print "invalid credentials"

        self.conn = sqlite3.connect('MainDB.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Log
             (ID INTEGER PRIMARY KEY, text TEXT, output TEXT, user TEXT)''')

        try:
            f = open("last.txt", "r")
            s = f.readline()
            if s.isdigit():
                self.lastRead = int(s)
            else:
                self.lastRead = int(s)
            f.close()
        except IOError as e:
            print "last.txt not found"
            self.lastRead = 0


    def getMessages(self):
        '''returns list, each elem [username, text, id].
        If no elems, returns []'''

        if time.time <= self.timerRead + READWAITTIME:
            #not enough time passed since last api call
            return []
        self.timerRead = time.time()
        commands = []
        try:
            print "LASTID:: " + self.lastRead
            messages = api.direct_messages(since_id = self.lastRead)
            for message in reversed(messages):
                if self.lastRead < int(message.id):
                    self.lastRead = int(message.id)
                text = message.text.replace("@" + self.botName + " ", "")
                user = message.sender.screen_name
                commands.append([user, text, int(message.id)])
        except tweepy.TweepError as e:
            print "Error getting commands: " + str(e.reason)
            return []
            # depending on TweepError.code, one may want to retry or wait
        return commands


    def SendMessage(self, idNum, text, response, user):
        '''returns true if message succsessfuly posted, false otherwise'''

        if time.time <= self.timerPost + POSTWAITTIME:
            #not enough time passed since last api call
            return False
        self.timerRead = time.time()
        try:
            api.send_direct_message(user,text=response)

            try:
                newlog = (idNum, text, response, user)
                self.cursor.execute('INSERT INTO stocks VALUES (?,?,?,?)', newlog)
            except Exception as e:
                print "sql stuff failed! oh no!"

            f = open("last.txt", "w")
            f.write(str(idNum))
            f.close()
            return True
        except tweepy.TweepError as e:
            print "Error trying to post status: " + str(e.reason)
    		#this may be improved upon to better handle specific errors.
            return False

    def SendPic(self, user, idNum, numTweets = 4):
        '''returns true if message succsessfuly posted, false otherwise'''

        if time.time <= self.timerPic + PICWAITTIME:
            #not enough time passed since last api call
            return False
        self.timerPic = time.time()

        #pull numTweets messages from the log.
        messagelist = []
        try:
            for row in cursor.execute('SELECT * FROM Log WHERE user=(?) ORDER BY ID ASC', (user,)):
                messagelist.append(">" + str(row[1]))
                messagelist.append(row[2])
        except Exception as e:
            print "sql stuff failed! oh no!"
        messagelist = messagelist[-1 * numTweets:]

        image = Img.gen(messagelist)
        try:
            image.save("123.png")
        except IOError:
            print("cannot convert")
            return False

        try:
            api.update_with_media(filename = "123.png", status = "Here is a highlight from @" + user)
            print('POSTED pic to ' + user)
            f = open("last.txt", "w")
            f.write(str(idNum))
            f.close()
            #do not update log when posting image. only track actual commands.
            return True

        except tweepy.TweepError as e:
            print "Error trying to post status: " + str(e.reason)
            return False
    		#this may be improved upon to better handle specific errors.










