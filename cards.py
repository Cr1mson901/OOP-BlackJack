import systemColors
import random
import ascii
import gui
import gamePlay
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
        self.cut_card = random.randint(15,37)

    def rebuild_check(self):
        if len(self.stack) <= self.cut_card:
            self.build(self.decks)

class hand:
    spacing = " " * 2
    def __init__(self,name="Dealer") -> None:
        self.cards = []
        self.count = 0
        self.name = name
    
    #TODO: add hit functionality
    def hit(self,shoe) -> bool:
        self.cards.append(shoe.stack.pop())
    
    def hand_print(self,my_hand=0) -> None:
        #Nested line comprehension that takes the each line of the ascii art and converts it to the correct suit
        if not my_hand:
            my_hand = self.cards
        self.name_tag(my_hand)
        cards = [[line.replace("♡",suits[card[1]][0]).replace(systemColors.RED, suits[card[1]][1])
                for line in ascii.numbers[card[0]]] 
                if card[0] != 1 else ascii.aces[card[1]] for card in my_hand]
        for pieces in zip(*cards):
            print(self.spacing.join(pieces))
    
    #Prints the first card and a facedown from the dealer
    def dealer_print(self) -> None:
        self.hand_print([self.cards[0],[14,"heart"]])
            
    #Prints a name tag for the cards to make it easier for the player to distinguish their cards        
    def name_tag(self,my_hand) -> None:
        print(f"{systemColors.RESET}{systemColors.RED}{self.name} {self.adder(my_hand)}")
        gui.color_scheme()

    #TODO: add bust check funtionality
    def busted(self):
        if self.count > 21:
            return True
        else:
            return False
    
    def adder(self,cards):
        aces = []
        numbers = []
        for card in cards:
            if card[0] == 1:
                aces.append(11)
            elif card[0] == 14:
                continue
            elif card[0] > 9:
                numbers.append(10)
            else:
                numbers.append(card[0])
        count = sum(numbers)
        while aces:
            if count + aces.pop() + len(aces) < 22:
                count += 11
            else:
                count += 1
        self.count = count
        return self.count