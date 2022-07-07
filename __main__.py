from Galaga.casting.cast import Cast
from Galaga.casting.player import Player
from Galaga.casting.enemy import Enemy
from Galaga.scripting.script import Script
from Galaga.scripting.control_actors_action import ControlActorsAction
from Galaga.scripting.move_actors_action import MoveActorsAction
from Galaga.scripting.handle_collisions_action import HandleCollisionsAction
from Galaga.scripting.draw_actors_action import DrawActorsAction
from Galaga.directing.director import Director
from Galaga.services.keyboard_service import KeyboardService
from Galaga.services.video_service import VideoService

def main():

    # create the cast
    cast = Cast()
    cast.add_actor("players", Player())
    cast.add_actor("enemies", Enemy())

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()