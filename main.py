import random
from art import logo
print(logo)
print("Welcome to Guess-The-Number-Game! I choose a number, and you guess the number!")
input("To start the game, press 'enter' to continue")
target = random.randint(1,100)
difficulty = input("First, choose your difficulty: 'easy' or 'hard'?\n")
user_choice = 0

LIVES = 0
if difficulty == "easy":
    LIVES = 10
elif difficulty == "hard":
    LIVES = 5

def int_checker():
    global user_choice
    while True:
        try:
            user_choice = int(input("Guess a number between 1 and 100: "))
            if user_choice > 100 or user_choice < 1:
                print("You have to guess a number between 1 and 100!")
            else:
                break
        except ValueError:
            print("Only whole numbers are allowed! No decimals, no symbols nor alphabets!")


end = False
while LIVES > 0 and end is False:
    print(f"You have {LIVES} lives left.")
    int_checker()
    if user_choice == target:
        print("You guessed the number! You win!")
        end = True
    elif user_choice != target:
        LIVES -= 1
        if LIVES == 0:
            print("Opps! You ran out of lives You lose!")
            print(f"The number was {target}")
            end = True
        elif user_choice > target:
            print("Too high!")
        elif user_choice < target:
            print("Too low!")