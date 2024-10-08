from platform   import system as system_name  # Returns the system/OS name
from subprocess import call   as system_call  # Execute a shell command
import systemColors

def clear_screen():
    # Clear screen command as function of OS
    command = 'cls' if system_name().lower().startswith('win') else 'clear'

    # Action
    system_call([command],shell=True)

def color_scheme(background = systemColors.WHITEB):
    #Sets the terminal to print in bold with a colored background
    print(f"{systemColors.B}{background}",end="")

#Prints the hands with dealers card hidden or uncovered depending on bool
def covered_print(covered,dealer,player):
    clear_screen()
    if covered:
        dealer.dealer_print()
    else:
        dealer.hand_print()
    player.hand_print()