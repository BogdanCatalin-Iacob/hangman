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
    pass
