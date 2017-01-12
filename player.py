
class Player:
    VERSION = "Default Python folding player +1"

    def betRequest(self, game_state):
        small_blind = game_state["small_blind"]
        print(small_blind)
        current_buy_in = game_state["current_buy_in"]
        print(current_buy_in)
        pot = game_state["pot"]
        print(pot)
        minimum_raise = game_state["minimum_raise"]
        print(minimum_raise)
        round = game_state["round"]
        print(round)
        dealer = game_state["dealer"]
        print(dealer)
        players = game_state["players"]
        print(players)
        in_action = game_state["in_action"]
        print(in_action)
        community_cards = game_state["community_cards"]
        print(community_cards)
        last_bet = players[in_action]["bet"]
        print(last_bet)
        return 10000

    def showdown(self, game_state):
        pass
