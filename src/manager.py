from src.card_dealer import Dealer


'''
Our game manager handles the game state, and deals cards

'''
class GameManager:
    def __init__(self):
        self.dealer = Dealer()

    def check_game_over(self, bettor, dummy):
        bettor_value = bettor.calculate_hand_value()
        dummy_value = dummy.calculate_hand_value()

        if bettor_value > 21:
            print("Bettor busts. Dummy wins.")
            return True
        elif dummy_value > 21:
            print("Dummy busts. Bettor wins.")
            return True
        elif bettor_value == dummy_value:
            print("Push!")
            return True
        elif dummy_value > bettor_value:
            print("Dummy wins.")
            return True
        elif bettor_value > dummy_value:
            print("Bettor wins.")
            return True
        return False
