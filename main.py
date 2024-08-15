import cards
import gui
import systemColors #A way to color outputs in the consol
import gamePlay
import time

def start() -> None:
    global player_name, shoe, dealer, player, bankroll
    player_name = input("Hello player, what is your name?\n").capitalize()
    gui.clear_screen()
    try:
        decks = int(input("How many decks would you like to be in the shoe(Default 3/Max 10)"))
        if decks > 10:
            raise Exception("Too many decks")
        if decks < 1:
            raise Exception("Not enough decks")
    except:
        decks = 3
    bankroll = gamePlay.bankroll_gen(player_name)
    #Generates two hands, one for the player and one for the Dealer
    player = cards.hand(player_name)
    dealer = cards.hand()
    #Makes a shoe entity so it can be filled with cards
    shoe = cards.shoe()
    shoe.build(decks)



def deal_cards():
    player.hit(shoe)
    dealer.hit(shoe)

if __name__ == "__main__":
    start()
    while bankroll > 0:
        #Resets hands
        dealer.cards = []
        player.cards = []
        
        #Acquires a valid bet from the player
        getting_bet = True
        while getting_bet:
            try:
                print(f"{player_name} you have ${bankroll}")
                bet = int(input(f"{systemColors.RESET}How much would you like to bet?\n"))
                if bet > bankroll:
                    raise Exception("Not enough money")
                elif bet < 1:
                    raise Exception("Not big enough of a bet")
                else:
                    getting_bet = False
            except:
                gui.clear_screen()
                print("Please input a valid bet")
       
        #Deals out two cards to the player and dealer
        for i in range(2):
            deal_cards()

        #Checks if Player or Dealer has a BlackJack before playing TODO: skip rest if blackjack
        if player.count == 21:
            print("Black Jack")
            bankroll += int(bet * 1.5)
        elif dealer.count == 21:
            print("You lose")
            bankroll -= bet
      
        #Displays the dealt out cards
        gui.covered_print(True,dealer,player)
        
        while input(f"{systemColors.RESET}Want to hit?")[0] != "n":
            player.hit(shoe)
            gui.covered_print(True,dealer,player)
            #Stops if hand busts
            if player.busted():
                break

        gui.covered_print(False,dealer,player)
        time.sleep(1)
        #Dealers turn if the player is still available
        if not player.busted():
            while dealer.count < 16:
                print(systemColors.RESET,end="")
                dealer.hit(shoe)
                gui.covered_print(False,dealer,player)
                time.sleep(1)
                if dealer.busted():
                    break
            #TODO: fix this so ties work
            print_max = lambda hand : print(f"{systemColors.RESET}{hand.name} is the winner of this hand with {hand.count}")
            print_max(max(dealer,player,key=lambda hand : hand.count))
        else:
            #Print busted message
            print(f"{systemColors.RESET}{player.name} busted so the Dealer wins this round")
            bankroll -= bet
        shoe.rebuild_check()
print(systemColors.RESET,end="")