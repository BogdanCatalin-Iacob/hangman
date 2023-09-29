'''
Simple hangman game
'''

from random import choice


def setup():
    '''
    Game settings
    Returns a random word and the initial number of tries
    '''
    word: str = choice(['bottle', 'screen', 'banana', 'building', 'raspberry', 'house'])
    tries: int = 5

    username: str = input('What is your name? >> ')
    print(f'Welcome to hangman, {username}!')

    data: dict = {
        'word': word,
        'tries': tries
    }
    return data


def run_game():
    '''
    Main game loop
    '''

    # get the settings
    data = setup()
    tries = data.get('tries')
    word = data.get('word')

    # keep track of the used letters
    guessed_letters: str = ''

    # game loop
    while tries > 0:
        blanks: int = 0  # underscores where letters should be

        print('Word: ', end='')
        for char in word:
            if char in guessed_letters:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print()  # adds an empty line

        guess: str = input('Enter a letter: ')
        if blanks == 0 or guess == word:
            print('You got it!')
            break

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print(f'You already used: "{guess}". Please try another letter!')
                continue

            guessed_letters += guess

            # decrease tries to end game
            if guess not in word:
                tries -= 1
                print(f'Sorry, that was wrong... ({tries} tries remaining)')

                if tries == 0:
                    print('No more tries remaining. Game Over')
                    break
        else:
            print('Only single letters or correct word allowed!\n Please, try again!')


if __name__ == '__main__':
    run_game()
