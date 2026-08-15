class PlayerNode:
    """node of the double linked list that holds one Player object"""

    def __init__(self, player):
        """Create a new node for the given player"""
        self._player = player
        self._next = None
        self._previous = None

    def __str__(self):
        """Return string for this node."""
        return f"PlayerNode({self._player})"

    @property
    def player(self):
        """Return the player stored in this node"""
        return self._player

    @property
    def next(self):
        """Return the next node in the list or None"""
        return self._next

    @next.setter
    def next(self, node):
        """Set the next node in the list"""
        self._next = node

    @property
    def previous(self):
        """Return the previous node in the list or None"""
        return self._previous

    @previous.setter
    def previous(self, node):
        """Set the previous node in the list."""
        self._previous = node

    @property
    def key(self):
        """Return the uid of the player, used as the key of the node."""
        return self._player.uid