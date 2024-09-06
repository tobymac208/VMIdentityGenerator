'''
    Created: 10/16/2022
    Generates a strong, random password.
    Author: Niklas Fernandez
'''

import random as rn

def create_phrase_password() -> str:
    '''
    Static function. Isn't specific to a class.

    Creates a password generated as a phrase. For instance "where-have-you-gone!" would be a password
        
    Arguments:
    Returns: 
    '''
    returns = None

    # read the list of words
    wordlist = None
    use_words = []
    number_to_add = rn.randint(1, 150000)

    WORDS_IN_PASSWORD = 4

    with open("PasswordGenerator/wordlist.txt", "r") as f:
        wordlist = f.readlines()
    
    for char in range(WORDS_IN_PASSWORD):
        use_words.append(rn.choice(wordlist).strip())
    
    returns = f"{use_words[0]}-{use_words[1]}-{use_words[2]}-{use_words[3]}{number_to_add}"
    return returns


def create_long_password() -> str:
    # Define what type of characters will be chosen.
    CHARACTERS_FOR_PASSWORD = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ1234567890$!@#'
    REQUIRED_LENGTH_OF_PASSWORD = 10
    MAXIMUM_LENGTH_OF_PASSWORD = 100

    length_of_password = REQUIRED_LENGTH_OF_PASSWORD
    generated_password = ''

    try:
        # Determine how many characters will be in the password.
        length_of_password = int(input(f'Number of characters for password (>= {REQUIRED_LENGTH_OF_PASSWORD} and <= {MAXIMUM_LENGTH_OF_PASSWORD}): '))
    except ValueError:
        print(f'Invalid character entered. Must be a number. Default length is {length_of_password}.')
    
    if length_of_password < REQUIRED_LENGTH_OF_PASSWORD or length_of_password > MAXIMUM_LENGTH_OF_PASSWORD:
        print(f'The length must be at least {REQUIRED_LENGTH_OF_PASSWORD} and cannot exceed {MAXIMUM_LENGTH_OF_PASSWORD} characters.\nGenerating a password that is long enough.')

        # Force the length to be at least at long as is required characters.
        length_of_password = REQUIRED_LENGTH_OF_PASSWORD

    for _ in range(length_of_password):
        generated_password += rn.choice(CHARACTERS_FOR_PASSWORD)

    return generated_password


def main():
    print(password_generator())


if __name__ == '__main__':
    main()
