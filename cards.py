import systemColors
import random
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
    def hit(self) -> None:
        self.cards.append()    
        self.count += 0
    
    def print(self) -> None:
        for pieces in zip(*self.cards):
            print(self.spacing.join(pieces))
