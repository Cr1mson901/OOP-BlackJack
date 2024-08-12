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
    def __init__(self,decks=3,cut=0) -> None:
        self.cut_card = cut
        self.decks = decks

    def build(self, amount) -> None:
        self.stack = []
        for i in range(amount):
            for card in range(2,14):
                for suit in suits.keys():
                    self.stack.append((card,suit))
            for suit in suits.keys():
                self.stack.append((1,suit))
        random.shuffle(self.stack)
        self.slice()

    def slice(self):
        cut_card = random.randint(15,37)

    def rebuild_check(self):
        if len(self.stack) <= self.cut_card:
            self.build(self.decks)

class hand:
    spacing = " " * 2
    def __init__(self,dealer=False) -> None:
        self.cards = []
        self.count = 0
    
    #TODO: add hit functionality
    def hit(self,shoe) -> None:
        self.cards.append(shoe.stack.pop())    
        self.count += 0
    
    def hand_print(self) -> None:
        #Nested line comprehension that takes the each line of the ascii art and converts it to the correct suit
        cards = [[line.replace("♡",suits[card[1]][0]).replace(systemColors.RED, suits[card[1]][1])
                for line in ascii.numbers[card[0]]] 
                if card[0] != 1 else ascii.aces[card[1]] for card in self.cards]
        for pieces in zip(*cards):
            print(self.spacing.join(pieces))
    
    def dealer_print(self) -> None:
        card = self.cards[0]
        if card[0] != 1:
            cards = [[line.replace("♡",suits[card[1]][0]).replace(systemColors.RED, suits[card[1]][1])
                for line in ascii.numbers[card[0]]]]
        else:
            cards = ascii.aces[card[1]]
        cards.append(ascii.face_down)
        for pieces in zip(*cards):
            print(self.spacing.join(pieces))
            
    def bust_check(self):
        pass
