class PlayerBNode:
    def __init__(self, player):
        self._player = player
        self._left = None
        self._right = None

    @property
    def player(self):
        return self._player

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @left.setter
    def left(self, left):
        self._left = left

    @right.setter
    def right(self, right):
        self._right = right