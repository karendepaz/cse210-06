class Moving_Object:
    """
    This moving_object class is the base for all the flying objects. Thus,
    it has one method, execute(), which should be overridden by derived classes.
    """

    def execute(self, cast, script):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        pass