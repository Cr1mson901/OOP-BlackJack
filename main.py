import cards
import gui
import systemColors #A way to color outputs in the consol
import random
import time

player_name = input("Hello player, what is your name?\n").capitalize()
#Randomizes the starting bankroll, making it kinda feel like slot wheel
bankroll = random.randint(500,5000)
for i in range(50):
    print(f"{player_name} you will be starting with ${random.randint(500,5000)}")
    time.sleep(.025)
    gui.clear_screen()
print(f"{player_name} you will be starting with ${bankroll}")

gui.color_scheme()
#Used for troubleshooting
player = cards.hand(player_name)
dealer = cards.hand()
shoe = cards.shoe()
shoe.build(3)
dealer.hit(shoe)
dealer.hit(shoe)
player.hit(shoe)
player.hit(shoe)
player.hand_print()
dealer.dealer_print()

while input(f"{systemColors.RESET}Want to hit?")[0] != "n":
    player.hit(shoe)
    gui.clear_screen()
    player.hand_print()