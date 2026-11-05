class PlayerBNode:
    """Node of binary search tree that hold one player object"""

    def __init__(self, player):
        """create a node for the given player with no children"""
        self._player = player
        self._left = None
        self._right = None

    @property
    def player(self):
        """return the player stored in this node"""
        return self._player

    @property
    def left(self):
        """return the root node of the left subtree or None"""
        return self._left

    @property
    def right(self):
        """return the root node of the right subtree or None"""
        return self._right

    @left.setter
    def left(self, node):
        """set the root node of the left subtree"""
        self._left = node

    @right.setter
    def right(self, node):
        """set the root node of the right subtree"""
        self._right = node