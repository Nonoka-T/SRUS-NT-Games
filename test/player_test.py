import unittest
from app.player import Player


class PlayerTest(unittest.TestCase):
    """Test the property of Player class"""

    def setUp(self):
        """Create an instance of Player class"""
        self.player = Player("1", "Nonoka Takahashi")

    def test_uid(self):
        """The uid should return the uid given to __init__"""
        self.assertEqual("1", self.player.uid)

    def test_name(self):
        """The name should return the name given to __init__"""
        self.assertEqual(self.player.name, "Nonoka Takahashi")

    def test_sort_players(self):
        players = [Player(player_id='01', player_name="Alice", score=10),
                   Player(player_id='02', player_name="Bob", score=5),
                   Player(player_id='03', player_name="Charlie", score=15),]

        sorted_players = sorted(players)
        manually_sorted_players = [Player(player_id='02', player_name="Bob", score=5),
                                   Player(player_id='01', player_name="Alice", score=10),
                                   Player(player_id='03', player_name="Charlie", score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        alice = Player(player_id='01', player_name="Alice", score=10)
        bob = Player(player_id='02', player_name="Bob", score=5)

        self.assertGreater(alice, bob)

    def test_sort_by_score(self):
        players = [Player(player_id='01', player_name="Alice", score=10),
                   Player(player_id='02', player_name="Bob", score=5),
                   Player(player_id='03', player_name="Charlie", score=15)]

        result = Player.sort_by_score(players)

        self.assertEqual([15, 10, 5], [player.score for player in result])



if __name__ == "__main__":
    unittest.main()