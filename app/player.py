import hashlib


class Player:
    def __init__(self, player_id, player_name):
        """Player unique id"""
        self._player_id = player_id
        self._player_name = player_name

    @classmethod
    def sha256_hash(cls, key):
        """
        return sha256 hash of the given key as integer.
        hexdigest() give a hexadecimal string so int(digest, 16) turns into a whole number.
        That number is far larger than 64bits and the built-in hash() would make it shorter to fit
        into 64 bits, so this method is called instead of hash().

        :param key: string to hash, normally player uid
        """
        digest = hashlib.sha256(key.encode()).hexdigest()
        return int(digest, 16)

    def __hash__(self):
        """
        Return the hash of this player, calculated from uid.
        Note that hash(player) makes this value shorter to fit into 64 bits.
        so the hash map call sha256_hash() directly.
        """
        return self.sha256_hash(self._player_id)

    def __str__(self):
        """Return the unique id of the player"""
        return f"{self._player_id} {self._player_name}"


    @property
    def uid(self):
        return self._player_id

    @property
    def name(self):
        return self._player_name

    @name.setter
    def name(self, player_name):
        """set a new name. Used when the hash map update a player."""
        self._player_name = player_name