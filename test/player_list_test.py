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
        self.assertEqual(self.player_list.head, self.player_list.tail)

    def test_add_to_head_when_list_is_not_empty(self):
        """new node should become the head and link to old head"""
        self.player_list.add_to_head(self.player1)
        self.player_list.add_to_head(self.player2)

        self.assertEqual(self.player2, self.player_list.head.player)
        self.assertEqual(self.player1, self.player_list.head.next.player)
        self.assertEqual(self.player_list.head, self.player_list.head.next.previous)
        self.assertEqual(self.player1, self.player_list.tail.player)

    def test_add_to_tail(self):
        """new node should become the tail nd link to the old tail"""
        self.player_list.add_to_tail(self.player1)
        self.player_list.add_to_tail(self.player2)

        self.assertEqual(self.player1, self.player_list.head.player)
        self.assertEqual(self.player2, self.player_list.tail.player)
        self.assertEqual(self.player_list.head, self.player_list.tail.previous)

    def test_remove_from_head(self):
        """The first node is removed and player is returned."""
        self.player_list.add_to_tail(self.player1)
        self.player_list.add_to_tail(self.player2)

        removed_player = self.player_list.remove_from_head()

        self.assertEqual(self.player1, removed_player)
        self.assertEqual(self.player2, self.player_list.head.player)
        self.assertIsNone(self.player_list.head.previous)

    def test_remove_from_tail(self):
        """the last node is removed and player is returned."""
        self.player_list.add_to_tail(self.player1)
        self.player_list.add_to_tail(self.player2)

        removed_player = self.player_list.remove_from_tail()

        self.assertEqual(self.player2, removed_player)
        self.assertEqual(self.player1, self.player_list.tail.player)
        self.assertIsNone(self.player_list.tail.next)

    def test_remove_from_head_when_list_is_empty(self):
        """remove from an empty list should return None"""
        self.assertIsNone(self.player_list.remove_from_head())


if __name__ == "__main__":
    unittest.main()