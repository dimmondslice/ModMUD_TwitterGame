from Command import Command

class Take(Command):
    """docstring for Take"""
    def __init__(self):
        super(Take, self).__init__()

        self.grammer = [["take"]]

    def Parse(self, _words, _dm, _player):
        response = "response"
        if len(_words) != 2:      
            response = "incorrect usage of take command"
        else:
            #build actor context for items available to pickup, only add items located in the room you are in, not the players inventory
            #adding this to the grammer is unnecesary but just reinforcing good practice.
            context = {}
            for actor in self.location.actors:
                context[actor.name] = actor
            self.grammer[1] = context.keys()

            if words[1] in self.grammer[1]:
                actor = context[words[1]]
                if actor.takeable == true:
                    _player.AddToInventory(actor)
                    actor.location.RemoveActor(actor)
                    actor.location = None

        self.twit.SendMessage(_dm[2], _dm[1], response, _dm[0])

    def TakeItem():
        pass
