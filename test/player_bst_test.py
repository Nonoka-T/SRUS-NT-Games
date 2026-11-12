import unittest

from app.player import Player
from app.player_bst import PlayerBST


class PlayerBSTInsertTest(unittest.TestCase):
    """tests inserting players into binary search tree"""

    def setUp(self):
        """create empty tree and 3 players used by every test"""
        self.bst = PlayerBST()
        self.nonoka = Player("1", "Nonoka")
        self.liam = Player("2", "Liam")
        self.christina = Player("3", "Christina")

    def test_new_tree_is_empty(self):
        """new tree has no root"""
        self.assertIsNone(self.bst.tree)

    def test_insert_into_empty_tree(self):
        """The first player become the root"""
        self.bst.insert(self.nonoka)

        self.assertEqual(self.nonoka, self.bst.tree.player)
        self.assertIsNone(self.bst.tree.left)
        self.assertIsNone(self.bst.tree.right)

    def test_insert_smaller_and_greater_name(self):
        """smaller name goes to the left and greater name goes to the right"""
        self.bst.insert(self.liam)
        self.bst.insert(self.nonoka)
        self.bst.insert(self.christina)

        self.assertEqual(self.christina, self.bst.tree.left.player)
        self.assertEqual(self.nonoka, self.bst.tree.right.player)

    def test_insert_into_subtree(self):
        """player is placed further down when the spot is already taken"""
        self.bst.insert(self.nonoka)
        self.bst.insert(self.liam)
        self.bst.insert(self.christina)

        self.assertEqual(self.liam, self.bst.tree.left.player)
        self.assertEqual(self.christina, self.bst.tree.left.left.player)

    def test_insert_duplicate_name(self):
        """player with a name already in the tree is not added again"""
        self.bst.insert(self.liam)
        self.bst.insert(Player("4", "Liam"))

        self.assertEqual(self.liam, self.bst.tree.player)
        self.assertIsNone(self.bst.tree.left)
        self.assertIsNone(self.bst.tree.right)


class PlayerBSTSearchTest(unittest.TestCase):
    """tests searching players by name using binary search tree"""

    def setUp(self):
        """create a tree holding 3 players"""
        self.bst = PlayerBST()
        self.nonoka = Player("1", "Nonoka")
        self.liam = Player("2", "Liam")
        self.christina = Player("3", "Christina")
        self.bst.insert(self.liam)
        self.bst.insert(self.nonoka)
        self.bst.insert(self.christina)

    def test_search_empty_tree(self):
        """searching an empty tree returns None"""
        empty_bst = PlayerBST()

        self.assertIsNone(empty_bst.search("Liam"))

    def test_search_root(self):
        """root node is returned when the name matches"""
        self.assertEqual(self.liam, self.bst.search("Liam").player)

    def test_search_left_and_right_subtree(self):
        """players in the left and right subtree can be found"""
        self.assertEqual(self.christina, self.bst.search("Christina").player)
        self.assertEqual(self.nonoka, self.bst.search("Nonoka").player)

    def test_search_unknown_name(self):
        """searching a name that isn't in the tree returns None"""
        self.assertIsNone(self.bst.search("Reika"))


if __name__ == '__main__':
    unittest.main()