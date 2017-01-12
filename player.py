import sys


class Player:
    VERSION = "fokin new strategy"

    weak_pair_hands = [
        (2, 7),
        (2, 8),
        (3, 8),
        (3, 7),
        (2, 6),
        (2, 9),
        (3, 9),
        (4, 9),
        (2, 10),
        (5, 9),
        (4, 7),
        (4, 8),
        (5, 8),
        (3, 6)
    ]

    # Constant holding the face cards one-char symbol and their value
    FACE_CARDS = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def unicode_repr(self, value):
        """
        Convert a value (string/int) to unicode object

        :param value: string or int
        :rtype: unicode obj
        """

        return unicode(str(value), "utf-8")

    def gen_diff_color_weak_pairs(self):
        """
        Generate weak pair hands. We use it when two cards are in different colors

        :rtype: list[tuple(unicode,unicode)]
        """

        diff_color_weak_pairs = []
        for face in self.FACE_CARDS.keys():
            for value in range(2, 6):
                new_unicode_pair = (self.unicode_repr(
                    face), self.unicode_repr(value))
                diff_color_weak_pairs.append(new_unicode_pair)
        return diff_color_weak_pairs

    def royal_flush(self, cards):
        return false

    def before_flop(self, hole_cards):
        """
        We check if we have weak hands in the beginning, and fold if we have. All in if not
        """
        our_tuple = (hole_cards[0]["rank"], hole_cards[1]["rank"])
        reversed_tuple = (our_tuple[1], our_tuple[0])

        if hole_cards[0]["suit"] == hole_cards[1]["suit"]:
            if our_tuple in self.weak_pair_hands or reversed_tuple in self.weak_pair_hands:
                return 0
        else:
            diff_color_weak_pairs = self.gen_diff_color_weak_pairs()
            if our_tuple in diff_color_weak_pairs or reversed_tuple in diff_color_weak_pairs:
                return 0
        return 10000

    def after_flop(self, hole_cards, community_cards):
        # if we have a match between hole and community cards in figure
        for hole_card in hole_cards:
            for com_card in community_cards:
                if hole_card["rank"] == com_card["rank"]:
                    return 10000

        # if we have a pair

        if hole_cards[0]["rank"] == hole_cards[1]["rank"]:
            return 10000

        # else:
        return 0

    def betRequest(self, game_state):
        # small_blind = game_state["small_blind"]
        current_buy_in = game_state["current_buy_in"]
        pot = game_state["pot"]
        minimum_raise = game_state["minimum_raise"]
        round = game_state["round"]
        dealer = game_state["dealer"]
        players = game_state["players"]
        in_action = game_state["in_action"]
        community_cards = game_state["community_cards"]
        last_bet = players[in_action]["bet"]
        hole_cards = players[in_action]["hole_cards"]
        print(hole_cards)

        if len(community_cards) == 0:
            return_bet = self.before_flop(hole_cards)
        else:
            return_bet = self.after_flop(hole_cards, community_cards)
        print(return_bet)
        print >> sys.stderr, return_bet
        return return_bet

    def showdown(self, game_state):
        pass
