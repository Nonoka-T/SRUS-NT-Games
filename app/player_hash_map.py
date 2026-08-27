from app.player import Player
from app.player_list import PlayerList

class PlayerHashMap:
    """
    Hash map that stores Player objects.
    Every index holds its own PlayerList and players whose keys give the same index
    are chained together in PlayerList.
    """
    SIZE = 10

    def __init__(self):
        """
        Create the hash map with SIZE empty PlayerList objects.
        loop is used so that every index gets own PlayerList.
        """
        self._hashmap = []
        for _ in range(self.SIZE):
            self._hashmap.append(PlayerList())

    def get_index(self, key):
        """
        return the index of the PlayerList this key belongs.
        :param key: uid string or Player object
        """
        if isinstance(key, Player):
            uid = key.uid
        else:
            uid = key

        return Player.sha256_hash(uid) % self.SIZE

    def _find_node(self, key):
        """
        Walk the PlayerList for this key and return the matching node.
        Return None when the key is not in the list.
        :param key: the uid of the player to look for
        """
        player_list = self._hashmap[self.get_index(key)]
        current_node = player_list.head
        while current_node is not None:
            if current_node.key == key:
                return current_node
            current_node = current_node.next
        return None

    def put(self, key, name):
        """
        add player to the PlayerList at the matching index.
        When the key is already stored, the player's name is updated instead of
        adding a second player with the same uid.
        :param key: uid of the player
        :param name:name of the player
        """
        node = self._find_node(key)
        if node is not None:
            node.player.name = name
        else:
            player_list = self._hashmap[self.get_index(key)]
            player_list.add_to_tail(Player(key, name))

    def get(self, key):
        """
        Return the player with the given uid.
        Return None when no player with uid is stored.
        :param key: the uid of the player to retrieve
        """
        node = self._find_node(key)
        if node is None:
            return None
        return node.player

    def remove(self, key):
        """
        Remove the player with the given uid.
        Return True when player was removed otherwise False.
        :param key: the uid of the player to remove
        """
        player_list = self._hashmap[self.get_index(key)]
        return player_list.remove_by_key(key)

    def size(self):
        """return how many players stored across all PlayerLists"""
        total = 0
        for player_list in self._hashmap:
            current_node = player_list.head
            while current_node is not None:
                total += 1
                current_node = current_node.next
        return total

    def display(self):
        """print the index and players of each PlayerList not empty"""
        for index in range(self.SIZE):
            player_list = self._hashmap[index]
            if not player_list.is_empty():
                print(f"Index: {index}")
                player_list.display()

    @property
    def hashmap(self):
        """return the list of PlayerList object"""
        return self._hashmap