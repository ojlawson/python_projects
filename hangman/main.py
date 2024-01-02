import random

# Use the 'word_list' from hangman_words.py
from hangman_words import word_list

# Select a random word and assign its length to var
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

# Use word length to create list with blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower() # Take in user letter input and make it lowercase

    # Duplicate guess handling
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # If letter is correct, update blank (_) list with letter
        if letter == guess:
            display[position] = letter

    # If guessed letter is incorrect
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")  
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the list elements turn it into a string
    print(f"{' '.join(display)}")

    # Check if all letters have been guessed
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages (ASCII art) from hangman_art.py
    from hangman_art import stages
    print(stages[lives])
