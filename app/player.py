class Player:
    def __init__(self, player_id, player_name):
        """Player unique id"""
        self._player_id = player_id
        self._player_name = player_name

    def __str__(self):
        """Return the unique id of the player"""
        return f"{self._player_id} {self._player_name}"

    @property
    def uid(self):
        return self._player_id

    @property
    def name(self):
        return self._player_name