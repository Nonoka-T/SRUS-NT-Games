import unittest

from app.player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player_name = self.player.name

    def test_name(self):
        self.assertEqual(self.player_name, "")

    def test_uid(self):
        self.assertEqual(self.player.uid, "")