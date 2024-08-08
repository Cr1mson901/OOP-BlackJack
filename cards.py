import systemColors
suits = {
    "heart":  ("♡",systemColors.RED),
    "diamond":("⬦",systemColors.RED),
    "spade":  ("♤",systemColors.BLACK),
    "club":   ("♧",systemColors.BLACK)
}
class deck:
    def __init__(self) -> None:
        pass

class hand:
    spacing = " " * 2
    def __init__(self) -> None:
        self.cards = []
        self.count = 0
    
    #TODO: add hit functionality
    def hit(self):
        self.cards.append()    
        self.count += 0
    
    def print(self):
        for pieces in zip(*self):
            print(self.spacing.join(pieces))
