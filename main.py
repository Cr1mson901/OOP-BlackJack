import cards
from ascii import faces, numbers #Art for the cards
import systemColors #A way to color outputs in the consol
from platform   import system as system_name  # Returns the system/OS name
from subprocess import call   as system_call  # Execute a shell command

background = systemColors.WHITEB
card_color = systemColors.RED
print(f"{systemColors.B}{background}")

suits = {
    "heart":  ("♡",systemColors.RED),
    "diamond":("⬦",systemColors.RED),
    "spade":  ("♤",systemColors.BLACK),
    "club":   ("♧",systemColors.BLACK)
}

def clear_screen():
    # Clear screen command as function of OS
    command = 'cls' if system_name().lower().startswith('win') else 'clear'

    # Action
    system_call([command])

clear_screen()

# #Prints cards in cards

cards = [[line.replace("♡","⬦") for line in numbers[6]],[line.replace("♡","♤").replace(systemColors.RED, systemColors.BLACK) for line in numbers[6]],numbers[10],faces["spade"]]
for pieces in zip(*cards):
    print("  ".join(pieces))