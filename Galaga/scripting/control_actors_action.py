import constants
from Galaga.scripting.moving_object import Moving_Object
from Galaga.shared.point import Point


class ControlActorsAction(Moving_Object):
    """
    An input action that controls the moving object.
    
    The responsibility of ControlActorsAction is to get the direction and move the object.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
        

        # snake = cast.get_first_actor("players")
        # snake.turn_head(self._direction)

        # # left-second player
        # if self._keyboard_service.is_key_down('j'):
        #     self._direction = Point(-constants.CELL_SIZE, 0)
        
        # # right-second player
        # if self._keyboard_service.is_key_down('l'):
        #     self._direction = Point(constants.CELL_SIZE, 0)
        
        # # up-second player
        # if self._keyboard_service.is_key_down('i'):
        #     self._direction = Point(0, -constants.CELL_SIZE)
        
        # # down-second player
        # if self._keyboard_service.is_key_down('k'):
        #     self._direction = Point(0, constants.CELL_SIZE)
        

        # # snake = cast.get_second_actor("players")
        # # snake.turn_head(self._direction)