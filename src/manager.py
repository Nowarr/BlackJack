class Manager:
    def __init__(self,dealer,dummy,bettor):
        self.dealer = dealer
        self.dummy = dummy
        self.bettor = bettor
        
    
    def game_status(self): # Prints status of game
        print("Dummy:",self.dummy.show_count())
        print("Bettor:",self.bettor.show_count())


    

    def check(self): # Checks who wins as dummy bets

        while True:
           
            self.game_status()

            if self.dummy.show_count() > 21:
                print("You Win")
                break

            elif self.bettor.show_count() > 21:
                print("Bust: You Lose")
                break
          
            elif self.bettor.show_count() <= self.dummy.show_count()  <= 21: # If dummy is greater than bettor and under 21
                if self.bettor.show_count() == self.dummy.show_count():
                    print("push")
                    break
                else:
                    print("You Lose")
                    break

            elif 16 >= self.dummy.show_count() < self.bettor.show_count() : # If dummy is less than bettor and under 16 
                self.dummy.receive_card(self.dealer.deal())
                self.check()
        

            elif 16 < self.dummy.show_count() < self.bettor.show_count(): # If dummy is greater than 16 by less than bettor
                print("You Win")
                break
            
            break
