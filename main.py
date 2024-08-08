import cards
import ascii #Art for the cards
import systemColors #A way to color outputs in the consol
from platform   import system as system_name  # Returns the system/OS name
from subprocess import call   as system_call  # Execute a shell command


def clear_screen():
    """
    Clears the terminal screen.
    """
    
    # Clear screen command as function of OS
    command = 'cls' if system_name().lower().startswith('win') else 'clear'

    # Action
    system_call([command])

clear_screen()

spacing = ' ' * 2  # Between cards.
cards = ascii.card_art[0], ascii.card_art[3], ascii.card_art[1]

for pieces in zip(*(card.splitlines() for card in cards)):
    print(spacing.join(pieces).format(systemColors.CYAN,systemColors.B,systemColors.WHITEB))



