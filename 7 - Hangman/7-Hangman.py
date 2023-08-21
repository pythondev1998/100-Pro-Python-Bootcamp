import random
from hangman_words import word_list
from hangman_art import stages, logo
print(logo)
#Generate a random word
chosen_word = random.choice(word_list)
print(chosen_word)

#Generate as many blanks as letters in word
word_lenght = len(chosen_word)
display =[]
for i in range (1,word_lenght+1):
    display.append("_")


#Ask the user to guess a letter
counter = word_lenght
lives = 6
end_of_game = False
while not end_of_game:
    guess_letter = input("Guess a letter: ").lower()

    if guess_letter in chosen_word:
        print(f"You've already guessed {guess_letter}")

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess_letter:
            display[position] = letter
            counter -= 1

    if guess_letter not in chosen_word:
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life")
        lives -= 1
        if(lives == 0):
            end_of_game = True
            print("Game over!")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
     end_of_game = True
     print("You win")

    print(stages[lives])
    
