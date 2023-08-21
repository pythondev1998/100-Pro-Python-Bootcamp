import random
from art import logo
#CONSTANTS

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Methods 

#Randomw number (answer)
def random_number():
    random_number = random.randint(1, 100)
    answer = random_number
    return answer

def game ():
    print(logo)
    answer = random_number()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficult. Type 'easy' or 'hard': ").lower()
    if(level == "easy"):
        attempts_reamining = EASY_LEVEL_TURNS
            
    elif (level == "hard"):
        attempts_reamining = HARD_LEVEL_TURNS

    compare(attempts_reamining, answer)
    
#Metodo que establece la dificultad y la retorna

#Metodo que hace la answer y pregunta el guess. (recibe la dificuktad tambien)


#Compare choose and guess number
def compare (attempts_reamining_param, answer_param):
    print(f"You have {attempts_reamining_param} attempts remaining to guess the number.")
    while attempts_reamining_param > 0:
        guess_number = int(input("Make a guess: ")) 
        if (guess_number == answer_param):
           print(f"You got it! The answer was {answer_param}.")
        elif (guess_number > answer_param):
            print("To high. Guess again.")
            attempts_reamining_param -= 1
            print(f"You have {attempts_reamining_param} attempts remaining to guess the number.")
        elif (guess_number < answer_param):
            print("To low. Guess again.")
            attempts_reamining_param -= 1
            print(f"You have {attempts_reamining_param} attempts remaining to guess the number.")
        if(attempts_reamining_param == 0):
            print("You lose")
game ()



