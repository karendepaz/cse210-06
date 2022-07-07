import constants
from Galaga.casting.actor import Actor
from Galaga.shared.point import Point

class Player(Actor): 
    """
    A player moves side to side and shoots at enemy. 

    The responsibility of Player is to move itself.
    """
    def __init__(self):
        super().__init__()
        self._trail = []
  
    def player(self):
        x = int(90)
        y = int(150)

        position = Point(x * constants.CELL_SIZE, y)
        velocity = Point(1 * constants.CELL_SIZE, 0)
        text = "V"
        color = constants.RED
        
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(color)

    # def get_head(self):
    #     return self._trail[0]

    # def turn_head(self, velocity):
        # self._trail[0].set_velocity(velocity)
    
    # def _prepare_trail(self):
    #     pass

    
