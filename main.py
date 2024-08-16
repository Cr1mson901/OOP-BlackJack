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
    #Generates two hands, one for the player and one for the Dealer
    player = cards.hand(player_name)
    dealer = cards.hand()
    player.bankroll = gamePlay.bankroll_gen(player.name)    
    #Makes a shoe entity so it can be filled with cards
    shoe = cards.shoe()
    shoe.build(decks)

def deal_cards():
    player.hit(shoe)
    dealer.hit(shoe)

def results(player,dealer):
    if player.count != dealer.count:
        print_max = lambda hand : print(f"{systemColors.RESET}{hand.name} is the winner of this hand with {hand.count}")
        winner = max(dealer,player,key=lambda hand : hand.count)
        print_max(winner)
        if winner == player:
            player.bankroll += player.bet
        else:
            player.bankroll -= player.bet
    else:
        print("Its a tie. The pot has been pushed")

if __name__ == "__main__":
    start()
    while player.bankroll > 0:
        #Resets hands
        dealer.cards = []
        player.cards = []
        
        #Gets bet
        gamePlay.get_bet(player)
        #Deals out two cards to the player and dealer
        for i in range(2):
            deal_cards()

        #Checks if Player or Dealer has a BlackJack before playing
        if player.count != 21 and dealer.count != 21:
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
            #Dealers turn if the player is still alive
            if not player.busted():
                while dealer.count < 16:
                    print(systemColors.RESET,end="")
                    dealer.hit(shoe)
                    gui.covered_print(False,dealer,player)
                    time.sleep(1)
                    #TODO: Dealer loses when busts
                    if dealer.busted():
                        break
                results(player,dealer)
            else:
                #Print busted message
                print(f"{systemColors.RESET}{player.name} busted so the Dealer wins this round")
                player.bankroll -= player.bet
        elif player.count == 21 and dealer.count == 21:
            print("Its a tie. The pot has been pushed")
        elif player.count == 21:
            print("Black Jack")
            player.bankroll += int(player.bet * 1.5)
        else:
            print("You lose")
            player.bankroll -= player.bet
        shoe.rebuild_check()
print(systemColors.RESET,end="")