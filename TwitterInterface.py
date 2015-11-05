import tweepy
import time
import Img
import sqlite3



class TwitterInterface(object):
    CONSUMER_KEY = "NZMk6RWDNI8d41GbTcZI4eWQf"
    CONSUMER_SECRET = "FQVENANJPofLA2JBifQZiMn04nTU0yDhxzwdJuTyG312mbenuJ"

    #static variable that holds the reference to this singleton, the only instance of TwitterInterface 
    ref = None

    def __init__(
                self,
                myapi,
                botName = 'SDADBOT'):
        '''set self.api,self.lastRead,self.timerRead,self.timerPost,self.botName
        key,secret,botname passed in to eventually support alt accounts'''
        self.timerRead = time.time()
        self.timerPost = 0
        self.timerPic = 0
        self.botName = botName
        
        self.api = myapi

        self.conn = sqlite3.connect('C:\\Users\\schatj5\\Documents\\GitHub\\TwitterGame\\MainDB.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Log
             (ID INTEGER PRIMARY KEY, text TEXT, output TEXT, user TEXT)''')
        self.READWAITTIME = 60
        self.POSTWAITTIME = 5
        self.PICWAITTIME = 5 #todo: unsure if its actually 5! must test!
        
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
        if time.time() <= self.timerRead + self.READWAITTIME:
            #not enough time passed since last api call
            return []
        self.timerRead = time.time()
        commands = []
        try:
            print "LASTID:: " + str(self.lastRead)
            messages = self.api.direct_messages(since_id = self.lastRead)
            time.sleep(61)
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
        '''returns true if message successfully posted, false otherwise'''

        if time.time() <= self.timerPost + self.POSTWAITTIME:
            #not enough time passed since last api call
            return False
        self.timerRead = time.time()
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
        '''returns true if message succsessfuly posted, false otherwise'''

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
            #do not update log when posting image. only track actual commands.
            return True

        except tweepy.TweepError as e:
            print "Error trying to post status: " + str(e.reason)
            return False
    		#this may be improved upon to better handle specific errors.










