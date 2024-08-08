import systemColors
import random
import ascii
suits = {
    "heart":  ("♡",systemColors.RED),
    "diamond":("⬦",systemColors.RED),
    "spade":  ("♤",systemColors.BLACK),
    "club":   ("♧",systemColors.BLACK)
}
class shoe:
    def __init__(self) -> None:
        pass

    def build(self, amount) -> None:
        self.stack = []
        for i in range(amount):
            for card in range(2,14):
                for suit in suits.keys():
                    self.stack.append((card,suit))
            for suit in suits.keys():
                self.stack.append((1,suit))
        random.shuffle(self.stack)

class hand:
    spacing = " " * 2
    def __init__(self) -> None:
        self.cards = []
        self.count = 0
    
    #TODO: add hit functionality
    def hit(self,shoe) -> None:
        self.cards.append(shoe.stack.pop())    
        self.count += 0
    
    def print(self) -> None:
        #Nested line comprehension that takes the each line of the ascii art and converts it to the correct suit
        cards = [[line.replace("♡",suits[card[1]][0]).replace(systemColors.RED, suits[card[1]][1])
                for line in ascii.numbers[card[0]]] 
                if card[0] != 1 else ascii.aces[card[1]] for card in self.cards]
        for pieces in zip(*cards):
            print(self.spacing.join(pieces))

