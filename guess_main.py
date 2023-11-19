'''
Programmer: SSgt Megan Schleicher
Date: 8/13/2023
Version: 1.0
Description: This game will demonstrate
more advanced techniques in object oriented
design by making a game that has classes
which will rely on each other. The game
will let the user guess a number between
1 and 100 and the computer will store guesses
and tell the user whether they have guessed
too low or too high.
'''

import pickle
import random
import os
from guess import Guess
from player import Player

#Constants
#Upon initialization computer generates random number
UPPER_BOUND = 100
LOWER_BOUND = 1
USER_GUESS_AMOUNT = 10
COMPUTER_PICKED_NUM = random.randint(LOWER_BOUND, UPPER_BOUND)
PLAYER_FILE_PATH = "pickle_file"

def validate_input():
    """will validate user input to make sure they are only entering what is expected
    will keep prompting user until correct input is entered.

    Returns:
        bool: true if the users input is valid, false if they need to be prompted again
    """
    while 1:
        try:
            #see if input is parsable into an integer
            user_input = int(input())
            if user_input < LOWER_BOUND or user_input > UPPER_BOUND:
                print(f'Please enter a number from {LOWER_BOUND} to {UPPER_BOUND}')
                continue
            return user_input

        #throw exception if they enter something that can't be an int
        except ValueError as err:
            print('Please enter a valid whole number')

def get_player_guess(used_player:Player):
    """get guess from player repeatedly throughout game"""

    #get input
    print(f"please enter a number between {LOWER_BOUND} and {UPPER_BOUND}: ")
    used_player.guess = validate_input()
    return used_player.guess

def store_players(current_user, player_list):
    """will handle writing player to file. Opens, writes to, and closes file"""        

    #write score and name to a file
    with open(PLAYER_FILE_PATH, 'w+b') as player_file:

        #add player to list
        #change number of guesses back to 10
        current_user.amount_of_guesses = USER_GUESS_AMOUNT
        player_list.append(current_user)

        #'dump' player object into pickle file
        pickle.dump(player_list, player_file)

        #make sure file is closed when finished so nothing breaks
        player_file.close()

def display_player_stats(current_user):
    """when it is determined that user exists, game will display statistics for that user"""

    print(f"\nHello {current_user.name}. Here are your "
          f"current stats \nWins: {current_user.number_of_wins} " +
          f"\nLosses: {current_user.number_of_fails}")

def get_player(user_name, player_list):
    """will return if player already exists based on username

    Args:
        player_name (string): players name

    Returns:
        Player: returns existing player or new player
    """

    #try to see if username given matches any existing players in the list
    #only run check if the list isn't empty
    if len(player_list) != 0:
        for player in player_list:
            if user_name == player.name:

                #return current player from list
                current_user = player

                #remove the player so there are no duplicates when loaded into file at end of game
                player_list.remove(current_user)

                return player
            
    #create new player to return since one doesn't exist already
    new_player = Player()
    new_player.name = user_name
    return new_player

def get_player_feedback(current_user:Player):
    """will take guess from player global variable, " +
    "return feedback by passing player guess into guess class"""

    #instansiate guess class
    guess = Guess()
    while 1:

        #pass guess to Guess class to see result
        if guess.guess_feedback(current_user.guess, COMPUTER_PICKED_NUM,
                                current_user.amount_of_guesses) is False:
            #decremenet guesses left
            if current_user.amount_of_guesses != 0:
                current_user.amount_of_guesses -= 1

                #if player fails
                if current_user.amount_of_guesses <= 0:

                    #number of fails increments
                    current_user.games_played += 1
                    current_user.number_of_fails += 1

                    print(f"{current_user.name}, you have run out of guesses, " +
                        "rerun file to play again.")
                    break
                    
                else:
                    #if player didn't win or lose, get more guesses
                    get_player_guess(current_user)

        #if user wins
        else:
            current_user.games_played += 1
            current_user.number_of_wins += 1
            break

    #return current user once game is over
    return current_user

def main():

    #instansiate list of players
    list_of_players = list()

    #deserialize pickle file at beginning of game
    #loop through stored objects in pickle file and store in list
    with open(PLAYER_FILE_PATH, 'r+b') as file:
        if os.path.getsize(PLAYER_FILE_PATH) > 0:
            
            #load existing players into list from pickle file
            list_of_players = pickle.load(file)

    #get player name
    player_name = input("Enter your name! ")

    #create new player object or get existing player
    player = get_player(player_name.lower(), list_of_players)

    #display stats for existing player
    display_player_stats(player)

    print(f"\n{player.name}, you have {player.amount_of_guesses} chances to guess the "
        f"random number the computer has generated")

    #get guess from player
    player.guess = get_player_guess(player)

    #give user feedback
    player = get_player_feedback(player)

    #store stats to pickle file
    store_players(player, list_of_players)

def usage():
    """prints guide on how to use arguments"""
    print("guess_main.py <guess> <name>")

if __name__ == "__main__":
    #avoid ctrl C / ctr D error
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        pass
