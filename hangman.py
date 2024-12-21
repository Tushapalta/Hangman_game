import random

def get_word():
    words = ['python', 'programme', 'computer', 'artificial', 'dataset', 'network', 'software']
    return random.choice(words).upper()

def display_hangman(tries):
    stages = [  # Final state: head, torso, both arms, both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # Head, torso, both arms, one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        # Head, torso, both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        # Head, torso, one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        # Head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        # Head
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        # Initial empty state
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]

def play_hangman():
    word = get_word()
    word_letters = set(word)  # Letters in the word
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters = set()  # Letters guessed by the user
    
    tries = 6  # Number of tries before game over
    
    # Game loop
    while len(word_letters) > 0 and tries > 0:
        print('\nYou have', tries, 'tries left.')
        print('Used letters:', ' '.join(used_letters))
        
        # What current word is (with underscores)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(display_hangman(tries))
        print('Current word:', ' '.join(word_list))
        
        # Get user input
        guess = input('Guess a letter: ').upper()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print('Good guess!')
            else:
                tries -= 1
                print('Wrong guess.')
        
        elif guess in used_letters:
            print('You already used that letter. Please try again.')
        
        else:
            print('Invalid character. Please try again.')
    
    # Game ended
    if tries == 0:
        print(display_hangman(0))
        print('Sorry, you died. The word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!!')

if __name__ == '__main__':
    print("Welcome to Hangman!")
    play_hangman()