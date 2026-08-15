import unittest

from app.player import Player
from app.player_list import PlayerList


class PlayerListTest(unittest.TestCase):
    """Tests inserting nodes into the double linked list."""

    def setUp(self):
        """Create empty list and two players used by every test."""
        self.player_list = PlayerList()
        self.player1 = Player("1", "Nonoka Takahashi")
        self.player2 = Player("2", "Edwin Tosen")

    def test_add_to_head_when_list_empty(self):
        """The new node should become the head of empty list."""
        self.player_list.add_to_head(self.player1)

        self.assertFalse(self.player_list.is_empty())
        self.assertEqual(self.player1, self.player_list.head.player)

    def test_add_to_head_when_list_is_not_empty(self):
        """The new node should become the head and link to old head"""
        self.player_list.add_to_head(self.player1)
        self.player_list.add_to_head(self.player2)

        self.assertEqual(self.player2, self.player_list.head.player)
        self.assertEqual(self.player1, self.player_list.head.next.player)
        self.assertEqual(self.player_list.head, self.player_list.head.next.previous)


if __name__ == "__main__":
    unittest.main()