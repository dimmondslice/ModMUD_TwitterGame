from Command import Command

class Inspect(Command):
    """docstring for Inspect"""
    def __init__(self):
        super(Inspect, self).__init__()

        self.grammer = [["inspect"]]
    def Parse(self, words, dm, player):
        response = "response"
        if(len(words) == 2):
            context = player.GetActorContext()
            if words[1] in context:
                response = "You inspect the " + words[1] + ":\n" + context[words[1]].description
            elif words[1] == "room":
                response = "You inspect the " + words[1] + ":\n"
                 #change the message if there is nothing in th room
                if(len(player.location.actors) == 0):
                    response += "    oh looks like there's nothing in here"

                for actor in player.location.actors:
                    response += "    " + actor.name +"\n"
            else:
                response = "There is no " + words[1] + " to inspect"

        else:
            response = "Incorrect usage of inspect command"

        self.twit.SendMessage(dm[2], dm[1], response, dm[0])





