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

#Prints the hands with dealers card hidden or uncovered depending on bool
def covered_print(covered):
    gui.clear_screen()
    if covered:
        dealer.dealer_print()
    else:
        dealer.hand_print()
    player.hand_print()

if __name__ == "__main__":
    start()
    while bankroll > 0:
        dealer.cards = []
        player.cards = []
        print(f"{player_name} you have ${bankroll}")
        getting_bet = True
        while getting_bet:
            try:
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
        #Used for troubleshooting
        dealer.hit(shoe)
        dealer.hit(shoe)
        player.hit(shoe)
        player.hit(shoe)

        if player.adder(player.cards) == 21:
            print("Black Jack")
            bankroll += int(bet * 1.5)
        elif dealer.adder(dealer.cards) == 21:
            print("You lose")
            bankroll -= bet
        dealer.dealer_print()
        player.hand_print()


        while input(f"{systemColors.RESET}Want to hit?")[0] != "n":
            player.hit(shoe)
            covered_print(True)
            if player.busted():
                break
        covered_print(False)
        time.sleep(1)
        if not player.busted():
            while dealer.adder(dealer.cards) < 16:
                print(systemColors.RESET,end="")
                dealer.hit(shoe)
                covered_print(False)
                time.sleep(1)
                if dealer.busted():
                    break
                            
            print_max = lambda hand : print(f"{systemColors.RESET}{hand.name} is the winner of this hand with {hand.count}")
            print_max(max(dealer,player,key=lambda hand : hand.count))
        else:
            #Print busted message
            print(f"{systemColors.RESET}{player.name} busted so the Dealer wins this round")
            bankroll -= bet
        shoe.rebuild_check()
print(systemColors.RESET,end="")