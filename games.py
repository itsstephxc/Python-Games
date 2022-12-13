# This is where we created the games
# I called on the 'answer' files to ensure it is recognized here when I use it

from answers import answers_list
import random

# Each game was 'defined' so that when we write the code on the main file we just make reference to it rather than
# mess with the entire file/code.

def magic_8_ball_game():
    while True:
        user_question = input('\nAsk Yes or No question: ')
        user_answer = random.choice(answers_list) # this assigned user_answer a random choice from 'answers'
        print(user_answer)
        next_step = input('\nDo you have another question? Yes/No: ')
        if next_step.lower() == 'yes': # the .lower() is what allows the user to use caps or not when answering
            continue # we created a while loop so that as long as the player wants to keep playing, we keep looping
        else:
            print('See You Later!\n')
            break # the loop breaks when they decide they don't want to play

def guess_the_number_game():
    possible_numbers = list(range(1,11,1)) # We made a list of numbers from 1 through 10 of which we will use one
    picked_number = random.choice(possible_numbers) # The computer will make a random choice from that list
    guesses = 0 # We are starting the users guesses at 0 because we want to give them only 3 tries to guess
    while True:
        guessed_number = int(input('\nGuess the number, between 1-10, we are thinking about: '))
        if guessed_number == picked_number:
            print('Yes! You WON!\n')
            break
        else:
            guesses += 1 # We are saying that if they guess wrong, we will add 1 to the number of tries
            if guesses == 3: # Once it reaches 3, they've had enough attempts and lose
                print(f'Nope. You LOST! We were thinking of {picked_number}\n')
                break

def rock_paper_scissors():
    while True:
        choices = ["rock", "paper", "scissors"] # Similar to Magic 8 and Guess the Number, we are making a list
        computer = random.choice(choices)
        player = None # We are establishing there is a player, but no assigned value
        while player not in choices: # We reference the player here and say that if they don't choose, we will keep asking
            player = input("\nChoose wisely - rock, paper, or scissors?: ").lower().strip()
# From here on out, we are listing out all the possible outcomes of the game
        if player == computer:
            print("We Chose: ", computer)
            print("You Chose: ", player)
            print("OoOOoOH, TIE!")

        elif player == "rock":
            if computer == "paper":
                print("We Chose: ", computer)
                print("You Chose: ", player)
                print("You LOSE!")
            if computer == "scissors":
                print("We Chose: ", computer)
                print("You Chose: ", player)
                print("You WIN!")

        elif player == "paper":
            if computer == "scissors":
                print("We Chose: ", computer)
                print("You Chose: ", player)
                print("You LOSE!")
            if computer == "rock":
                print("We Chose: ", computer)
                print("You Chose: ", player)
                print("You WIN!")

        elif player == "scissors":
            if computer == "rock":
                print("We Chose: ", computer)
                print("You Chose: ", player)
                print("You LOSE!")
            if computer == "paper":
                print("We Chose: ", computer)
                print("You Chose: ", player)
                print("You WIN!")

        play_again = input("\nWould you like to play again? (yes/no)")

        if play_again.lower() != "yes":
            break
    print("\nThanks for playing - See you later!")

