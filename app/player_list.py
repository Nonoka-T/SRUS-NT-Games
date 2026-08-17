from app.player_node import PlayerNode


class PlayerList:
    """
    double linked list that stores Player objects.
    The list can be walked from the head to tail and back again.
    """

    def __init__(self):
        """Create an empty list."""
        self._head = None
        self._tail = None

    def is_empty(self):
        """Return True when the list doesn't contain any node."""
        return self._head is None

    def add_to_head(self, player):
        """Insert a new node with the given player at the head of list"""
        new_node = PlayerNode(player)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.previous = new_node
            self._head = new_node

    def add_to_tail(self, player):
        """Insert a new node with the given player at the tail of list"""
        new_node = PlayerNode(player)
        if self.is_empty():
            self._tail = new_node
            self._head = new_node

        else:
            new_node.previous = self._tail
            self._tail.next = new_node
            self._tail = new_node

    def remove_from_head(self):
        """remove the first node and return player, return None when the list is empty."""
        if self.is_empty():
            return None

        removed_node = self._head
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = removed_node.next
            self._head.previous = None
            removed_node.next = None
        return removed_node.player

    def remove_from_tail(self):
        """remove the last node and return player, return None when the list is empty."""
        if self.is_empty():
            return None

        removed_node = self._tail
        if self._head is self._tail:
            self._tail = None
            self._head = None
        else:
            self._tail = removed_node.previous
            self._tail.next = None
            removed_node.previous = None
        return removed_node.player


    @property
    def head(self):
        """Return the current node of the list."""
        return self._head

    @property
    def tail(self):
        """Return the last node of the list."""
        return self._tail