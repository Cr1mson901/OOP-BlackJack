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

if __name__ == "__main__":
    start()

#Used for troubleshooting
dealer.hit(shoe)
dealer.hit(shoe)
player.hit(shoe)
player.hit(shoe)
dealer.dealer_print()
player.hand_print()


while input(f"{systemColors.RESET}Want to hit?")[0] != "n":
    player.hit(shoe)
    gui.clear_screen()
    dealer.dealer_print()
    player.hand_print()
gui.clear_screen()
dealer.hand_print()
player.hand_print()
time.sleep(1)
while dealer.adder(dealer.cards) < 16:
    print(systemColors.RESET,end="")
    dealer.hit(shoe)
    gui.clear_screen()
    dealer.hand_print()
    player.hand_print()
    time.sleep(1)

print_max = lambda hand : print(f"{systemColors.RESET}{systemColors.RED}{hand.name} is the winner of this hand")
print_max(max(dealer,player,key=lambda hand : hand.count))

print(systemColors.RESET,end="")