
import random
'''
This hangman code allows the player to guess letters and progressively 
reveals the word or ends the game when the player either 
correctly guesses the word or runs out of lives.
'''
stages = ['''
 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
==========
''', '''
 +---+
 |   |
 0   |
/|\  |
/    |
     |
==========
''', '''
 +---+
 |   |
 0   |
/|\  |
     |
     |
==========
''', '''
 +---+
 |   |
 0   |
/|   |
     |
     |
==========
''', '''
 +---+
 |   |
 0   |
 |   |
     |
     |
==========
''', '''
 +---+
 |   |
 0   |
     |
     |
     |
==========
''', '''
 +---+
 |   |
     |
     |
     |
     |
==========
''', '''
 +---+
     |
     |
     |
     |
     |
==========
''']
print("Welcome to the hangman game")
word_list = ["Python", "Java", "JavaScript","Kotlin","swift"]
chosen_word = random.choice(word_list).lower()  # Convert chosen word to lowercase
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Testing code
print(f"Pssst, the solution is {chosen_word}.")
# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter!\n").lower()

    # Check the guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost the game")

    # Join the elements in the list and turn it into a string
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])
