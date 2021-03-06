from Command import Command

#Command type object that will print the description of an actor in the current context when a player requests it
#See Command class for general info on how commands work

class Inspect(Command):
    """docstring for Inspect"""
    def __init__(self):
        super(Inspect, self).__init__()

        self.name = "inspect"
        self.grammer = [["inspect"]]
        self.description = "Examine an object or space thoroughly. 'inspect [item name]' or 'inspect room'."

    #called from the Players ParseMessage(), this is overridden by the other commands
    def Parse(self, words, _dm, player):
            #words = list of strings that have been tolower()ed
            #_directMessage = [userName, messagetext, messageid,]
            #_player = player type, the player who called this command
        response = "response"

        if(len(words) == 2):
            context = player.GetActorContext()
            if words[1] in context:
                response = "You inspect the " + words[1] + ":\n" + context[words[1]].description

            #special case if the player is trying to inspect what is in the room
            elif words[1] == "room":
                response = "You inspect the " + player.location.name + ":\n"
                 #change the message if there is nothing in th room
                if(len(player.location.actors) == 0):
                    response += "    oh looks like there's nothing in here"
                #otherwise loop through every actor in the room
                for actor in player.location.actors:
                    response += "    " + actor.name +"\n"
            else:
                response = "There is no " + words[1] + " to inspect"

        else:
            response = "Incorrect usage of inspect command. Try 'inspect' [item] or 'inspect' 'room'"

        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])





