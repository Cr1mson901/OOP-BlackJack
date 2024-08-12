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