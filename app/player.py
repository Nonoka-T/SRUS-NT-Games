class Player:
    def __init__(self, player_id, player_name):
        self.player_id = player_id
        self.player_name = player_name

    def uid(self):
        return self.player_id

    def name(self):
        return self.player_name