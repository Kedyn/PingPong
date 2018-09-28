# based on:
#   https://nicolasivanhoe.wordpress.com/2014/03/10/game-scene-manager-in-python-pygame/


class Scene():
    """Game scene template."""

    def __init__(self, director):
        self.director = director

    def keydown(self, key):
        """Keydown event."""
        pass

    def keyup(self, key):
        """Keyup event."""
        pass

    def update(self):
        """Updates."""
        pass

    def render(self):
        """Render."""
        pass
