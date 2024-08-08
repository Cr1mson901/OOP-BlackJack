import cards
from ascii import card_art #Art for the cards
import systemColors #A way to color outputs in the consol
from platform   import system as system_name  # Returns the system/OS name
from subprocess import call   as system_call  # Execute a shell command

spacing = ' ' * 2  # Between cards.
background = systemColors.WHITEB
card_color = systemColors.RED
print(f"{systemColors.B}")



def clear_screen():
    # Clear screen command as function of OS
    command = 'cls' if system_name().lower().startswith('win') else 'clear'

    # Action
    system_call([command])

clear_screen()

cards = card_art[0], card_art[3], card_art[1]

print(f"{card_color}{background}")
for pieces in zip(*(card.splitlines() for card in cards)):
    print(spacing.join(pieces))



