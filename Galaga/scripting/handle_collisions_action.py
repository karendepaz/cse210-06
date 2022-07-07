from Galaga.casting.enemy import Enemy
import constants
from Galaga.casting.actor import Actor
from Galaga.scripting.moving_object import Moving_Object
from Galaga.shared.point import Point

class HandleCollisionsAction(Moving_Object):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the player collides
    with the enemy, or the enemy collides, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_game_over(cast)
    
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            players = cast.get_actors("players")
            enemies = cast.get_actors("enemy")
            for player in players:

                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                position = Point(x, y)

                message = Actor()
                message.set_text("Game Over!")
                message.set_position(position)
                cast.add_actor("messages", message)