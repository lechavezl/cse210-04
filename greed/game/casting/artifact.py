from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):

    def __init__(self):
        super().__init__()
        self._message = ""
        self._points = 0
        self._gem = "*"
        self._rock = "▯"
    
    def set_message(self, message):
        self._message = message

    def get_message(self):
        return self._message
    
    def get_gem(self):
        
        return self._gem
    
    def get_rock(self):
        return self._rock

    def calculate_points(self):

        if self.get_text() == "*":
            self._points += 1
        
        elif self.get_text() == "▯":
            self._points -= 1
        
        return self._points