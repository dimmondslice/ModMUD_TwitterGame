import tweepy
import time
import Img
import sqlite3
import os
from Singleton import Singleton

@Singleton
class TwitterInterface(object):
    CONSUMER_KEY = "NZMk6RWDNI8d41GbTcZI4eWQf"
    CONSUMER_SECRET = "FQVENANJPofLA2JBifQZiMn04nTU0yDhxzwdJuTyG312mbenuJ"

    def Setup(self, myapi, botName = 'SDADBOT'):
        """
        Sets initial parameters for the class
        To be called only once when first setting up TwitterInterface
        """
        self.READWAITTIME = 61
        self.POSTWAITTIME = 6
        self.PICWAITTIME = 5

        self.botName = botName
        self.api = myapi

        self.timerRead = 0
        self.timerPost = 0
        self.timerPic = 0

        self.conn = sqlite3.connect( os.path.dirname(__file__) + '\\MainDB.db' )
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
        """
        Gets direct messages sent to bot from twitter since last call
        Returns list of [username, text, id]. If no elems, returns []
        """
        if time.time() <= self.timerRead + self.READWAITTIME:
            #not enough time passed since last api call
            return []
        self.timerRead = time.time()
        commands = []
        try:
            messages = self.api.direct_messages(since_id = self.lastRead)
            for message in reversed(messages):
                #todo: check if user is in whitelist before adding!
                if self.lastRead < int(message.id):
                    self.lastRead = int(message.id)
                text = message.text.replace("@" + self.botName + " ", "")
                user = message.sender.screen_name
                commands.append([user, text, int(message.id)])
        except tweepy.TweepError as e:
            print "Error getting commands: " + str(e.reason)
            return []
            # depending on TweepError.code, one may want to retry or wait
        print "Read in " + str(len(commands)) + " commands"
        return commands


    def SendMessage(self, idNum, text, response, user):
        """
        Continuously attempts to call __SendMessage until it succeeds.
        Failure not nessessarily due to error.
        Twitter can be unresponsive, need to wait for rate limit, ect.
        """
        while True:
            #keep attempting until returns successfully.
            if self.__SendMessage(idNum, text, response, user):
                break

    def __SendMessage(self, idNum, text, response, user):
        """
        Sends response as a direct message to user, then updates log
        Returns true if message successfully posted, false otherwise
        """
        if time.time() <= self.timerPost + self.POSTWAITTIME:
            #not enough time passed since last api call
            return False
        self.timerPost = time.time()
        try:
            self.api.send_direct_message(user,text=response)

            try:
                newlog = (idNum, text, response, user)
                self.cursor.execute('INSERT INTO Log VALUES (?,?,?,?)', newlog)
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
        """
        Continuously attempts to call __SendPic until it succeeds.
        Failure not nessessarily due to error.
        Twitter can be unresponsive, need to wait for rate limit, ect.
        """
        while True:
            #keep attempting until returns successfully.
            if self.__SendPic(user, idNum, numTweets):
                break

    def __SendPic(self, user, idNum, numTweets):
        """
        Tweets pic of last numTweets messages to user. Doesn't update Log.
        Returns true if message successfully posted, false otherwise
        """
        if time.time() <= self.timerPic + self.PICWAITTIME:
            #not enough time passed since last api call
            return False
        self.timerPic = time.time()

        #pull numTweets messages from the log.
        messagelist = []
        try:
            for row in self.cursor.execute('SELECT * FROM Log WHERE user=(?) ORDER BY ID ASC', (user,)):
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
            self.api.update_with_media(filename = "123.png", status = "Here is a highlight from @" + user)
            print('POSTED pic to ' + user)
            f = open("last.txt", "w")
            f.write(str(idNum))
            f.close()
            return True

        except tweepy.TweepError as e:
            print "Error trying to post status: " + str(e.reason)
            return False
    		#this may be improved upon to better handle specific errors.










