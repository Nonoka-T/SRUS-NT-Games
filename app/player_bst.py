from app.player_bnode import PlayerBNode

class PlayerBST:
    """
    binary search tree to store Player objects
    Player's name is used as the key of each node.
    """

    def __init__(self):
        """create an empty tree"""
        self._tree = None

    @property
    def tree(self):
        """Return the root node of the tree, None when the tree is empty"""
        return self._tree