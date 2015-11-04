from Tkinter import *
import threading
import tweepy
import os.path
#import TwitterInterface
from webbrowser import open_new_tab

#Open an error file for debugging.
sys.stderr = open("errorfile.txt","w")

#userArray stores the list of players in the current instance of the game.
userArray = []

#consumerToken and consumerSecret are used for Twitter Authentication. They are unique to our app and should not be changed.
consumerToken = "NZMk6RWDNI8d41GbTcZI4eWQf"
consumerSecret = "FQVENANJPofLA2JBifQZiMn04nTU0yDhxzwdJuTyG312mbenuJ"

#authentication is a part of the Twitter API. It is the gatekeeper between our app and the user account.
authentication = tweepy.OAuthHandler(consumerToken, consumerSecret)

#authCheck is used to determine if the program has authenticated a user account before. 
authCheck = os.path.isfile("previous.auth")
userCheck = os.path.isfile("user.list")

#accessKey and accessSecret are the user side pieces of Twitter Authentication. authName is used to hold the name of the authenticated user.
accessKey = ""
accessSecret = ""
authName = "None"

if authCheck:
    #A file containing previous authentication information exists.
    #We now try to read in previous.auth and its stored user access information.
    with open("previous.auth") as f:
        #Read in all lines from the auth file.
        authParams = [x.strip('\n') for x in f.readlines()]
    accessKey = authParams[0]
    accessSecret = authParams[1]
    #Load the authentication parameters into the API authentication.
    authentication.set_access_token(accessKey, accessSecret)
    
if userCheck:
    #A file containing previous authentication information exists.
    #We now try to read in previous.auth and its stored user access information.
    with open("user.list") as f:
        #Read in all lines from the auth file.
        userArray = [x.strip('\n') for x in f.readlines()]
    
#theAPI is our API object from tweepy. It takes in as much authentication information as we've accumulated at this time.
theAPI = tweepy.API(authentication)

#If our user is authenticated already, then we can load 
try:
    authName = theAPI.me().name
except tweepy.TweepError:
    authName = "None"

#A boolean to determine whether or not a game has been started
startedGame = False
    
def AddUser(listBox, entryBox):
    '''This function adds the user name in entryBox to the userArray. It is also listed in the listBox.'''
    if entryBox.get() != "" and entryBox.get() not in userArray:
        listBox.insert(END, entryBox.get())
        userArray.append(entryBox.get())
        
    entryBox.delete(0,END)
    with open("user.list","w+") as file:
        for name in userArray:
            file.write(name)
            if name is  not userArray[-1]:
                file.write("\n")
    
def RemoveUser(listBox):
    '''This function removes the user name from the listBox, and from the userArray.'''
    if userArray != []:
        userArray.remove(listBox.get(ANCHOR))
    listBox.delete(ANCHOR)
    with open("user.list","w+") as file:
        for name in userArray:
            file.write(name)
            if name is not userArray[-1]:
                file.write("\n")
    

def GetAccessToken(accessCode):
    '''This function opens the page to get an access code from the host client's Twitter account. It also opens the entry box to input the access code.'''
    try:
        redirectURL = authentication.get_authorization_url()
    except tweepy.TweepError:
        print "Error! Failed to get request token."
        return
    open_new_tab(redirectURL)
    accessCode.configure(state=NORMAL)
    accessCode.delete(0,END)
    
def ConfirmAccessToken(accessCode,botRunner):
    '''This function attempts to authenticate the access code provided in the accessCode entry box. If successful, it sets the botRunner variable to the newly authenticated account.'''
    try:
        token = authentication.get_access_token(accessCode.get())
    except tweepy.TweepError:
        print "Error! Failed to get access token."
        return
    botRunner.set(theAPI.me().name)
    accessCode.configure(state=DISABLED)
    with open("previous.auth","w+") as file:
        file.write(token[0]+'\n')
        file.write(token[1]+'\n')

class App(threading.Thread):
    '''This is the central GUI class for the host client.'''
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.rootWindow.quit()
    
    def run(self):
        #Create the root window. This is where all of the other GUI elements will be placed. It's unresizable at the moment, and the close button breaks the main loop.
        self.rootWindow = Tk()
        self.rootWindow.resizable(width=FALSE, height=FALSE)
        self.rootWindow.protocol("WM_DELETE_WINDOW", self.callback)
        
        #botRunner is a string variable that holds the name of the currently authenticated user.
        self.botRunner=StringVar()
        self.botRunner.set(authName)
        
        #The main window is broken up into 4 frames.
        #00 holds the host client name [IDname], the label prompt for that name [IDprompt], and the button to change the host client account [IDrequest].
        #10 holds the entry field for the access code [accessCode] and the button to validate the access code [validate].
        #01 holds the entry field to add a new player [nameEntry] and the button to confirm that player [enterButton].
        #11 holds the list box of currently added users [userListBox] and the button to remove the currently selected user from the list box [remove].
        self.frame00 = Frame(self.rootWindow, height=1, bd=1, relief=SUNKEN)
        self.frame01 = Frame(self.rootWindow, height=1, bd=1, relief=SUNKEN)
        self.frame10 = Frame(self.rootWindow, height=1, bd=1, relief=SUNKEN)
        self.frame11 = Frame(self.rootWindow, height=1, bd=1, relief=SUNKEN)
        
        #The frames are then added to the main window here. The names are based on their grid coordinates.
        self.frame00.grid(row=0, column=0)
        self.frame01.grid(row=0, column=1)
        self.frame10.grid(row=1, column=0)
        self.frame11.grid(row=1, column=1)
        
        accessCode = Entry(self.frame10, exportselection = 0,state=DISABLED)
        accessCode.pack()
        
        validate = Button(self.frame10, text = "Validate", command = lambda ac=accessCode, b = self.botRunner: ConfirmAccessToken(ac,b) ).pack()
        
        IDprompt = Label(self.frame00, text = "Current ID:").pack()
        IDname = Label(self.frame00, textvariable = self.botRunner).pack()
        IDrequest = Button(self.frame00, text = "Set Output Account", command = lambda ac = accessCode: GetAccessToken(ac)).pack()
        
        nameEntry = Entry(self.frame01, exportselection = 0)
        nameEntry.pack()
        
        userListBox = Listbox(self.frame11)
        
        enterButton = Button(self.frame01, text = "Add User", command = lambda listBox=userListBox, e=nameEntry: AddUser(listBox,e)).pack()
        
        userListBox.pack()
        
        for name in userArray:
            userListBox.insert(END, name)
        
        remove = Button(self.frame11, text = "Remove User", command = lambda listBox=userListBox: RemoveUser(listBox) ).pack()
        
        startGame = Button(self.rootWindow, text = "Start Game", command = lambda listBox=userListBox: RemoveUser(listBox) )
        startGame.grid(row=2, column=0)
        
        self.rootWindow.mainloop()


app = App()

twitFace = None

while twitFace is None:
    if gameStarted:
        twitFace = TwitterInterface()