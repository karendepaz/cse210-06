from Galaga.scripting.moving_object import Moving_Object


class DrawActorsAction(Moving_Object):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        self._video_service.clear_buffer()
        players = cast.get_actors("players")
        enemies = cast.get_actors("enemies")

        for player in players:
            playing = player.player()
            messages = cast.get_actors("messages")

            self._video_service.draw_actors(playing)
            self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()