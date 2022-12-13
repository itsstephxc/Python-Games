# MAIN
#  To start of we import what we will be calling on throughout the code
# We first import the games we created on the 'games' page

from games import guess_the_number_game
from games import magic_8_ball_game
from games import rock_paper_scissors

while True:
        user_answers = int(input('''
    
     Welcome to Group 4's Project!
    
     Which game would you like to play?
    
        1) Magic 8 Ball
        2) Guess the Number
        3) Rock, Paper, Scissors
        4) Exit
    
    '''))
# We assign a number to the game and end with 'continue' so that the user is always rerouted to the Main Menu

        if user_answers == 1:
            magic_8_ball_game()
        elif user_answers == 2:
            guess_the_number_game()
        elif user_answers == 3:
            rock_paper_scissors()
            continue
        else:
            break