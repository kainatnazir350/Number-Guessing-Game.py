#Python Number guessing Game

import random

lowest_num =1
higest_num =100
answer =random.randint(lowest_num, higest_num)
guesses =0
is_running = True

print("python Number Guessing Game")
print (f"Select a number between {lowest_num} and {higest_num}")

while is_running:
    
    guess = input("Ëntre your guess:")
    
    if guess.isdigit():
        guess =int(guess)
        guesses+=1
        
        if guess <lowest_num or guess >higest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num}and {higest_num}")
        elif guess<answer:
            print("Too low ! Try again!")
        elif guess>answer:
            print("Too high!Try again!")
        else:
           print(f"Correct! The answer was {answer}")
           print(f"Number of guesses {guesses}")    
    else:
        
        print("Invalid guess")
        print(f"Please select a number between {lowest_num}and {higest_num}")

