import random
import time
import gui
import systemColors
#Randomizes the starting bankroll, making it kinda feel like slot wheel

def bankroll_gen(name):
    bankroll = random.randint(500,5000)
    for i in range(50):
        print(f"{name}, you have ${random.randint(500,5000)}")
        time.sleep(.025)
        gui.clear_screen()
    return bankroll

#Acquires a valid bet from the player
def get_bet(player,getting_bet=True):
    while getting_bet:
        global bet
        try:
            print(f"{player.name}, you have ${player.bankroll}")
            bet = int(input(f"{systemColors.RESET}How much would you like to bet?\n"))
            if bet > player.bankroll:
                raise Exception("Not enough money")
            elif bet < 1:
                raise Exception("Not big enough of a bet")
            else:
                getting_bet = False
        except:
            gui.clear_screen()
            print("Please input a valid bet")
    player.bet = bet