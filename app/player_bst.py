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

    def search(self, name):
        """
        return the node whose key matches name or None when it isn't found.
        """
        return self._search(self._tree, name)

    def _search(self, node, name):
        """search the subtree starting at node for the given name"""
        # reached the end of tree or found the name
        if node is None or node.player.name == name:
            return node

        # name is smaller so it can only be in the left subtree
        if name < node.player.name:
            return self._search(node.left, name)

        # name is greater so can only be in the right subtree
        return self._search(node.right, name)