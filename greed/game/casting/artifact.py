from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _points (int): Total for each artifact.
        _point (int): The number of points the artifacts are worth.
        _.
    """

    def __init__(self):
        super().__init__()
        self._message = ""
        self._points = 0
        self._point = 0
        # self._gem = "*"
        # self._rock = "O"
    
    # def get_gem(self):
        
    #     return self._gem
    
    # def get_rock(self):
    #     return self._rock

    def calculate_points(self):

        if self.get_text() == "*":
            self._point = 1
            self._points = 0 + self._point
        
        elif self.get_text() == "O":
            self._point = -1
            self._points = 0 + self._point
        
        return self._points