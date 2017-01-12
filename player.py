import sys
import random


class Player:
    VERSION = "haha strategy"

    # Constant holding the weak pair hands when we have the same color
    WEAK_PAIR_HANDS = [
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

    # constant with strong 5 card hands
    STRONG_HANDS = [
        [{"rank": x, "suit": "hearts"} for x in ["A", "K", "Q", "J", "10"]], #royal flush hearts
        [{"rank": x, "suit": "clubs"} for x in ["A", "K", "Q", "J", "10"]], #royal flush clubs
        [{"rank": x, "suit": "diamonds"} for x in ["A", "K", "Q", "J", "10"]], #royal flush diamonds
        [{"rank": x, "suit": "spades"} for x in ["A", "K", "Q", "J", "10"]] #royal flush spades
    ]
        
        #[{"rank": x, "suit": "hearts"} for x in cards[]] for cards in ["K", "Q", "J", "10", "9", "8", "7", "6"][k:k+5] for k in range(3)
        

    # Constant holding the face cards one-char symbol and their value
    FACE_CARDS = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def same(self, expected_cards, actual_cards):
        have_it = [False, False, False, False, False]
        for act_card in actual_cards:
            for index, exp_card in enumerate(expected_cards):
                if act_card["rank"] == exp_card["rank"] and act_card["suit"] == exp_card["suit"]:
                    have_it[index] = True
        have_all = True
        for have_this_card in have_it:
            have_all = have_all and have_this_card
        return have_all

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

    def before_flop(self, hole_cards):
        """
        We check if we have weak hands in the beginning, and fold if we have. All in if not
        """
        our_tuple = (hole_cards[0]["rank"], hole_cards[1]["rank"])
        reversed_tuple = (our_tuple[1], our_tuple[0])

        if hole_cards[0]["suit"] == hole_cards[1]["suit"]:
            if our_tuple in self.WEAK_PAIR_HANDS or reversed_tuple in self.WEAK_PAIR_HANDS:
                return 0
        else:
            diff_color_weak_pairs = self.gen_diff_color_weak_pairs()
            if our_tuple in diff_color_weak_pairs or reversed_tuple in diff_color_weak_pairs:
                return 0
        return 10000

    def after_flop(self, hole_cards, community_cards):
        # if we have strong hands
        for hand in self.STRONG_HANDS:
            if self.same(hand, hole_cards + community_cards):
                return 10000

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

        if len(community_cards) == 0:
            return_bet = self.before_flop(hole_cards)
        else:
            return_bet = self.after_flop(hole_cards, community_cards)

        if return_bet == 10000:  # if we want to go full retard, pls don't
            return_bet = current_buy_in - last_bet + \
                minimum_raise + random.randint(50, 300)

        print(return_bet)
        print(community_cards)
        print >> sys.stderr, return_bet
        return return_bet

    def showdown(self, game_state):
        pass
