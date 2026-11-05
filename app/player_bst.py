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

    def insert(self, player):
        """
        Insert player into the tree using the player's name as the key.
        when a player with the sane name is already in the tree,
        nothing is added so tree has no duplicates.
        """
        self._tree = self._insert(self._tree, player)

    def _insert(self, node, player):
        """
        insert the player into the subtree starting at node.
        return the root node of the subtree after insert.
        """
        #　empty spot found so the new node go here
        if node is None:
            return PlayerBNode(player)

        if player.name < node.player.name:
            node.left = self._insert(node.left, player)
        elif player.name > node.player.name:
            node.right = self._insert(node.right, player)
        #　same name do nothing so no duplicate node is made
        return node