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

        else:
            response = "Incorrect usage of inspect command"

        self.twit.SendMessage(dm[2], dm[1], response, dm[0])





