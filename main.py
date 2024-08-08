import cards
import gui
from ascii import faces, numbers #Art for the cards
import systemColors #A way to color outputs in the consol

gui.color_scheme()

# #Prints cards in cards
hand = cards.hand()
hand.cards = [[line.replace("♡","⬦") for line in numbers[6]],[line.replace("♡","♤").replace(systemColors.RED, systemColors.BLACK) for line in numbers[6]],numbers[10],faces["spade"]]
hand.print()