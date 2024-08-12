import cards
import gui
import systemColors #A way to color outputs in the consol
import gamePlay

def start() -> None:
    global player_name, shoe, dealer, player, bankroll
    player_name = input("Hello player, what is your name?\n").capitalize()
    gui.clear_screen()
    try:
        decks = int(input("How many decks would you like to be in the shoe(Default 3/Max 10)"))
        if decks > 10:
            raise Exception("Too many decks")
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
player.hand_print()
dealer.dealer_print()

while input(f"{systemColors.RESET}Want to hit?")[0] != "n":
    player.hit(shoe)
    gui.clear_screen()
    dealer.dealer_print()
    player.hand_print()