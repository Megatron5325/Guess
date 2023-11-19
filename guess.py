'''
Programmer: SSgt Meagn Schleicher
Date: 8/13/2023
Version: 1.0
Description: This class will handle guesses. 
It will store the number the computer picked, 
and keep track of the guesses made by the user.
'''

class Guess:
    """this class will represent a guess and all the methods that will be used to 
    rturn feedback to the user about their guess"""

    def __str__(self):
        return str(self.guess_counter)

    def guesses_left(self):
        """returns the number of guess left to the user"""
        return self.guess_counter.__str__

    def guess_feedback(self, player_guess, computer_picked_number, amount_of_guesses) -> bool:
        """will give the user feedback as to whether they guess too high, 
        too low, or the right answer.

        Args:
            guess: guess
            computer_picked_number: integer

        Returns:
            string
        """
        if player_guess > computer_picked_number:
            print(f'Too high! You have {amount_of_guesses - 1} guesses left.')
            return False
        elif player_guess < computer_picked_number:
            print(f'Too low! You have {amount_of_guesses - 1} guesses left.')
            return False
        else:
            print("Correct! Well done. You are MASTER WIZARD OF THE UNIVERSE.")
            return True
        