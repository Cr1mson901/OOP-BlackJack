import random
import time
import gui
#Randomizes the starting bankroll, making it kinda feel like slot wheel
def bankroll_gen(name):
    bankroll = random.randint(500,5000)
    for i in range(50):
        print(f"{name} you will be starting with ${random.randint(500,5000)}")
        time.sleep(.025)
        gui.clear_screen()
    print(f"{name} you will be starting with ${bankroll}")
    return bankroll

def total(cards):
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
    return count