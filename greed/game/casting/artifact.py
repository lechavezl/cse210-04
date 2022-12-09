from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        super().__init__(): Constructor of the Actor class
        _points (int): Total for each artifact.
        _point (int): The number of points the artifacts are worth.
    """

    def __init__(self):
        super().__init__()
        self._points = 0
        self._point = 0


    def calculate_points(self):
        """
        Determine if the artifact is a gem (*) or a rock (O) to calculate the points
        The player when touches one of them.
        
        If it is a gem the artifact worth 1 points, if it is a rock, loses a point.

        Return:
            Return a number (int) 
        """

        if self.get_text() == "*":
            self._point = 1
            self._points = 0 + self._point
        
        elif self.get_text() == "O":
            self._point = -1
            self._points = 0 + self._point
        
        return self._points