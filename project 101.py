import random
def roll_a_dice(min,max):
    while True:
        print("Rolling dice...")
        print(f"Your number :{random.randint(min,max)}")
        choice = input ("Do you want to Roll the dice again?")
        if choice.lower() == 'n':
            break

roll_a_dice(1,6)
