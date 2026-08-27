import io
import unittest
from contextlib import redirect_stdout

from app.player import Player
from app.player_hash_map import PlayerHashMap
from app.player_list import PlayerList


class PlayerHashTest(unittest.TestCase):
    """Test the hash added to the Player class"""

    def test_hash_is_deterministic(self):
        """same uid should always give the same hash."""
        self.assertEqual(Player.sha256_hash("1"), Player.sha256_hash("1"))
        self.assertNotEqual(Player.sha256_hash("1"), Player.sha256_hash("2"))

    def test_hash_is_not_made_shorter(self):
        """The hash should be bigger than a 64 bit value."""
        self.assertGreater(Player.sha256_hash("1"), 2 ** 64)


class PlayerHashMapTest(unittest.TestCase):
    """Tests adding, retrieving and removing players in the hash map."""

    def setUp(self):
        """Create an empty hash map used by every test."""
        self.hash_map = PlayerHashMap()

    def find_key_with_the_same_index(self, key):
        """
        return another uid that lands on the same index as key.
        Two keys landing on the same index is called a collision.
        :param key: the uid to share an index with
        """
        wanted_index = self.hash_map.get_index(key)
        number = 2
        while number < 1000:
            candidate = str(number)
            if candidate != key:
                if self.hash_map.get_index(candidate) == wanted_index:
                    return candidate
            number += 1
        return None

    def capture_display(self):
        """
        Run display() and return everything it printed as one string.
        redirect_stdout catches the printing so the test can check it.
        """
        output = io.StringIO()
        with redirect_stdout(output):
            self.hash_map.display()
        return output.getvalue()

    def test_new_hash_map_has_ten_separate_player_lists(self):
        """
        new hash map is empty and holds SIZE different PlayerList objects,
        not ten references to the same one.
        """
        self.assertEqual(0, self.hash_map.size())
        self.assertEqual(10, len(self.hash_map.hashmap))
        for player_list in self.hash_map.hashmap:
            self.assertIsInstance(player_list, PlayerList)

        # Adding to one PlayerList must not fill any of the others
        self.hash_map.hashmap[0].add_to_tail(Player("1", "Nonoka Takahashi"))
        self.assertFalse(self.hash_map.hashmap[0].is_empty())
        for index in range(1, 10):
            self.assertTrue(self.hash_map.hashmap[index].is_empty())

    def test_get_index(self):
        """
        Every key gives an index inside the hash map and Player gives the same index as uid.
        """
        for number in range(100):
            index = self.hash_map.get_index(str(number))
            self.assertGreaterEqual(index, 0)
            self.assertLess(index, PlayerHashMap.SIZE)

        player = Player("1", "Nonoka Takahashi")
        self.assertEqual(self.hash_map.get_index("1"), self.hash_map.get_index(player))

    def test_put_and_get(self):
        """
        Players can be added and retrieved, size counts them across the PlayerLists
        and each player is node in PlayerList.
        """
        self.hash_map.put("1", "Nonoka Takahashi")
        self.hash_map.put("2", "Edwin Tosen")
        self.hash_map.put("3", "Cameron Hendrikse")
        index = self.hash_map.get_index("1")

        self.assertEqual(3, self.hash_map.size())
        self.assertEqual("Nonoka Takahashi", self.hash_map.get("1").name)
        self.assertEqual("1", self.hash_map.hashmap[index].head.key)

    def test_put_with_existing_key_updates_the_name(self):
        """putting a stored uid updates the name and add no player"""
        self.hash_map.put("1", "Nonoka Takahashi")
        self.hash_map.put("1", "Nonoka Sawahata")

        self.assertEqual("Nonoka Sawahata", self.hash_map.get("1").name)
        self.assertEqual(1, self.hash_map.size())

    def test_remove(self):
        """
        removed player is gone, and an unknown uid returns False from remove
        and None from get instead of raising an error
        """
        self.hash_map.put("1", "Nonoka Takahashi")

        self.assertTrue(self.hash_map.remove("1"))
        self.assertIsNone(self.hash_map.get("1"))
        self.assertEqual(0, self.hash_map.size())

        self.assertFalse(self.hash_map.remove("5"))
        self.assertIsNone(self.hash_map.get("5"))

    def test_two_keys_with_the_same_index_are_chained(self):
        """
        Two keys with the same index are chained in one PlayerList,
        both can be retrieved and removing one keep the other.
        """
        other_key = self.find_key_with_the_same_index("1")
        self.assertIsNotNone(other_key)

        self.hash_map.put("1", "Nonoka Takahashi")
        self.hash_map.put(other_key, "Edwin Tosen")
        index = self.hash_map.get_index("1")
        player_list = self.hash_map.hashmap[index]

        # Both players are nodes in the same PlayerList
        self.assertEqual("1", player_list.head.key)
        self.assertEqual(other_key, player_list.head.next.key)
        self.assertEqual("Nonoka Takahashi", self.hash_map.get("1").name)
        self.assertEqual("Edwin Tosen", self.hash_map.get(other_key).name)

        # Removing one of them leaves the other one in place
        self.hash_map.remove("1")
        self.assertIsNone(self.hash_map.get("1"))
        self.assertEqual("Edwin Tosen", self.hash_map.get(other_key).name)
        self.assertEqual(1, self.hash_map.size())

    def test_display(self):
        """
        display prints the index and the player of PlayerList that holds a player,
        and prints nothing for the empty one
        """
        self.assertEqual("", self.capture_display())

        self.hash_map.put("1", "Nonoka Takahashi")
        index = self.hash_map.get_index("1")
        printed = self.capture_display()

        self.assertIn(str(index), printed)
        self.assertIn("Nonoka Takahashi", printed)
        # One line for the index and one line for the player
        self.assertEqual(2, len(printed.splitlines()))


if __name__ == "__main__":
    unittest.main()