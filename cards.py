import systemColors
suits = {
    "heart":  ("♡",systemColors.RED),
    "diamond":("⬦",systemColors.RED),
    "spade":  ("♤",systemColors.BLACK),
    "club":   ("♧",systemColors.BLACK)
}
class shoe:
    def __init__(self) -> None:
        self.stack = []

    def build(self, amount) -> None:
        deck = []
        for i in range(amount):
            for card in range(2,11):
                for suit in suits.keys():
                    deck.append()

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
