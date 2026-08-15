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


if __name__ == "__main__":
    unittest.main()