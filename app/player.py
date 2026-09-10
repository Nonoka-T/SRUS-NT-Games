import hashlib


class Player:
    def __init__(self, player_id, player_name, score=0):
        """
        Create player
        :param player_id: unique id
        :param player_name: player name
        :param score: score of the player, 0 when it's not given
        """
        self._player_id = player_id
        self._player_name = player_name
        self._score = score

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

    @classmethod
    def sort_by_score(cls, players):
        """Return a new list of players sorted by score, highest first"""
        if len(players) <= 1:
            return players

        middle = len(players) // 2
        pivot = players[middle]
        rest = players[:middle] + players[middle + 1:]

        higher = []
        lower = []
        for player in rest:
            if player > pivot:
                higher.append(player)
            else:
                lower.append(player)

        return cls.sort_by_score(higher) + [pivot] + cls.sort_by_score(lower)

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

    def __repr__(self):
        """return description of player used"""
        return (f"{self.__class__.__name__} (name='{self._player_name}', "
                f"uid='{self._player_id}', score={self._score})")

    def __lt__(self, other):
        """return True when player's score is lower than others."""
        return self._score < other._score

    def __eq__(self, other):
        """return True when player has the same uid."""
        return self._player_id == other.uid

    @property
    def uid(self):
        return self._player_id

    @property
    def name(self):
        return self._player_name

    @property
    def score(self):
        return self._score

    @name.setter
    def name(self, player_name):
        """set a new name. Used when the hash map update a player."""
        self._player_name = player_name

    @score.setter
    def score(self, value):
        """set a new score.
        :param value: positive whole number
        :raises ValueError: when the value isn't positive
        """
        if value <= 0:
            raise ValueError("score must be a positive value")
        self._score = value