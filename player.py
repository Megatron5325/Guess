'''
Programmer: SSgt Megan Schleicher
Date: 8/13/2023
Version: 1.0
Description: This class will be
the player. It will be an object
that can be used in guess_main
'''

# what is a player?
class Player:
    """A model of a player for the guessing game"""
    def __init__(self, name = "N/A", games_played = 0, number_of_fails = 0, number_of_wins = 0, guess = 0, amount_of_guesses = 10):
        self.name = name
        self.games_played = games_played
        self.number_of_fails = number_of_fails
        self.number_of_wins = number_of_wins
        self.guess = guess
        self.amount_of_guesses = amount_of_guesses

    # JAEGER: Adding this method to show you something
    def __str__(self) -> str:
        return f"{self.name} | Wins: {self.number_of_wins}\n Losses:{self.number_of_fails}\n Games Played: {self.games_played}"
    