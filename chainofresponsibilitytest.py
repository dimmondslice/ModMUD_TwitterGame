import sys
import traceback

BOTNAME = "SDADBOT"

class Link(object):
    def __init__(self, handler):
        self._handler = handler
        self._next = None

    def handle(self, obj):
        if not self._handler.process(obj):
            if self._next:
                return self._next.handle(obj)
            else:
                return False
        return True

    def addHandler(self, newHandler):
        if self._next:
            self._next.addHandler(newHandler)
        else:
            self._next = newHandler


class JumpCommand(object):
    #request is a CommandRequest object
    def process(self,request):
        if request.getText().lower() == "jump":
            #request is a Jump Command, Process!
            print "user @" + request.getUser() + " has jumped!"
            return True
        else:
            return False

class WaveCommand(object):
    #request is a CommandRequest object
    def process(self,request):
        if request.getText().lower() == "wave":
            #request is a Wave Command, Process!
            print "user @" + request.getUser() + " has waved!"
            return True
        else:
            return False

class SitCommand(object):
    #request is a CommandRequest object
    def process(self,request):
        if request.getText().lower() == "sit":
            #request is a Wave Command, Process!
            print "user @" + request.getUser() + " has sat!"
            return True
        else:
            return False


class CommandRequest(object):

    def __init__ (self, u, a, i):
        #needs to be updated to sanitize the input to the text field.
        #should all but alphanumeric characters be ignored?
        self.__user = u 								   # person who sent it
        self.__text = a.replace("@" + BOTNAME + " ", "")   # core of the txt
        self.__id = i                                      # message id number

    def getUser(self):
        return self.__user

    def getText(self):
        return self.__text

    def getID(self):
        return self.__id


def main():
    Chain = Link(JumpCommand())
    Chain.addHandler(Link(WaveCommand()))
    Chain.addHandler(Link(SitCommand()))

    try:
        while True:
            str = raw_input("Enter command")
            req = CommandRequest("user1", str, 123)
            if not Chain.handle(req):
                #no valid command found - default case
                print "Invalid Command"
    except Exception:
        traceback.print_exc()
        sys.exit()

if __name__ == '__main__':
    main()


