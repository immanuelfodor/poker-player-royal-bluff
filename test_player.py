import unittest
import copy
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.cards = [
            {
                "rank": "10",
                "suit": "hearts"
            },
            {
                "rank": "J",
                "suit": "hearts"
            },
            {
                "rank": "Q",
                "suit": "hearts"
            },
            {
                "rank": "K",
                "suit": "hearts"
            },
            {
                "rank": "A",
                "suit": "hearts"
            }
        ]

    def test_same_same(self):
	cards2 = self.cards;
        self.assertTrue(self.player.same(self.cards, cards2))

    def test_same_diff(self):
        cards2 = copy.deepcopy(self.cards)
	cards2[1]["suit"] = "clubs"
        self.assertFalse(self.player.same(self.cards, cards2))

if __name__ == '__main__':
    unittest.main()
