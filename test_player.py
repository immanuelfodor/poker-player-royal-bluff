import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def test_same_same(self):
	cards1 = [
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
	cards2 = cards1;
        player = Player()
        self.assertTrue(player.same(cards1, cards2))

    def test_same_diff(self):
        cards1 = [
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
        cards2 = [
            {
                "rank": "10",
                "suit": "clubs"
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

        player = Player()
        self.assertFalse(player.same(cards1, cards2))

if __name__ == '__main__':
    unittest.main()
