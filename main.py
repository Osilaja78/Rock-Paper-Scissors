# Rock papaer scissors game

import random

possible_options = [ "R", "P", "S" ]

def initialize():
    global player_hand, cpu_hand
    print("Welcome to rock paper scissors game")
    print("*** Pick an option ***")
    print("R = ROCK")
    print("P = PAPER")
    print("S = SCISSORS")

    while True:
        player_hand = input("\nPick a hand: ").upper()
        if (player_hand == "R" or player_hand == "P" or player_hand == "S"):
            
            # Print results
            print("Your hand: ", player_hand)
            print("Computer hand: ", cpu_hand)
            print(check_winner(player_hand, cpu_hand))
            break
        else:
            print("Invalid input, please try again")
        
cpu_hand = random.choice(possible_options)    

# Create a function to check for winner
def check_winner(player_hand, cpu_hand):
    
    if(player_hand == "R" and cpu_hand == "S"):
        print("Congratulations, you won.")
        replay()

    elif(player_hand == "S" and cpu_hand == "R"):
        print("Sorry, you lost.")
        replay()

    elif(player_hand == "R" and cpu_hand == "P"):
        print("Sorry, you lost.")
        replay()

    elif(player_hand == "P" and cpu_hand == "R"):
        print("Congratulations, you won.")
        replay()

    elif(player_hand == "P" and cpu_hand == "S"):
        print("Sorry, you lost.")
        replay()

    elif(player_hand == "S" and cpu_hand == "P"):
        print("Congratulations, you won.")
        replay()

    else:
        print("It's a tie.")
        replay()


def replay():
    print("\nWould you like to play another game,")
    print("Y = yes or N = no")
    replay_input = input("Please select an option: ").upper()
    if replay_input == "Y":
        initialize()
    elif replay_input == "N":
        exit()
    else:
        print("Invalid input, please try again")
        replay()
        
initialize()
