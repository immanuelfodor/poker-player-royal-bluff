
class Player:
    VERSION = "Default Python folding player +2"

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
        weak_hands = [
            [2,7],[2,8],[3,8],[3,7],[2,6],[2,9],[3,9],[4,9],[2,10],[5,9],[4,7],[4,8],[5,8],[3,6]
        ]

        for card in weak_hands:
            if hole_cards[0]["rank"] == card[0] or hole_cards[1]["rank"] == card[1] or hole_cards[0]["rank"] == card[1] or hole_cards[1]["rank"] == card[0]:
                return 0
        
        return 10000

    def showdown(self, game_state):
        pass
