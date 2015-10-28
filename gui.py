from Tkinter import *
import threading
import tweepy
from webbrowser import open_new_tab

sys.stderr = open("errorfile.txt","w")
#Stored information:
#[0] = consumer_token
#[1] = consumer_secret
#Add this later, once authentication is working



userarray = []

consumer_token = "NZMk6RWDNI8d41GbTcZI4eWQf"
consumer_secret = "FQVENANJPofLA2JBifQZiMn04nTU0yDhxzwdJuTyG312mbenuJ"

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

api = tweepy.API(auth)

#from user, get the following:
#auth.access_token
#auth.access_token_secret

def put(lb, e):
    if e.get() != "" and e.get() not in userarray:
        lb.insert(END, e.get())
        userarray.append(e.get())
        
    e.delete(0,END)
    print userarray
    
def rementry(lb):
    if userarray != []:
        userarray.remove(lb.get(ANCHOR))
    lb.delete(ANCHOR)
    
    print userarray

def getAccessToken(name,b,ac):
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print 'Error! Failed to get request token.'
        return
    open_new_tab(redirect_url)
    ac.configure(state=NORMAL)
    ac.delete(0,END)
    
def confirmAccessToken(ac,b):
    try:
        auth.get_access_token(ac.get())
    except tweepy.TweepError:
        print 'Error! Failed to get access token.'
        return
    b.set(api.me().name)
    ac.configure(state=DISABLED)

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()
    
    def run(self):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.botrunner =StringVar()
        self.botrunner.set("None")
        
        self.frame00 = Frame(self.root, height=1, bd=1, relief=SUNKEN)
        self.frame01 = Frame(self.root, height=1, bd=1, relief=SUNKEN)
        self.frame10 = Frame(self.root, height=1, bd=1, relief=SUNKEN)
        self.frame11 = Frame(self.root, height=1, bd=1, relief=SUNKEN)
        
        self.frame00.grid(row=0, column=0)
        self.frame01.grid(row=0, column=1)
        self.frame10.grid(row=1, column=0)
        self.frame11.grid(row=1, column=1)
        
        
        
        accessCode = Entry(self.frame10, exportselection = 0,state=DISABLED)
        accessCode.pack()
        validate = Button(self.frame10, text = "Validate", command = lambda ac=accessCode, b = self.botrunner: confirmAccessToken(ac,b) ).pack()
        
        IDprompt = Label(self.frame00, text = "Current ID:").pack()
        IDname = Label(self.frame00, textvariable = self.botrunner).pack()
        IDrequest = Button(self.frame00, text = "Set Output Account", command = lambda n=IDname, b = self.botrunner, ac = accessCode: getAccessToken(n,b,ac)).pack()
        
        nameentry = Entry(self.frame01, exportselection = 0)
        nameentry.pack()
        
        userlist = Listbox(self.frame11)
        
        enterbutton = Button(self.frame01, text = "Add User", command = lambda lb=userlist, e=nameentry: put(lb,e)).pack()
        
        userlist.pack()
        
        remove = Button(self.frame11, text = "Remove User", command = lambda lb=userlist: rementry(lb) ).pack()
        

        
        self.root.mainloop()


app = App()
print('Now we can continue running code while mainloop runs!')