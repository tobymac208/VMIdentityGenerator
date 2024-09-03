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
    pass

def create_long_password():
    # Define what type of characters will be chosen.
    CHARACTERS_FOR_PASSWORD = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ1234567890$!@#'
    REQUIRED_LENGTH_OF_PASSWORD = 10

    length_of_password = REQUIRED_LENGTH_OF_PASSWORD
    generated_password = ''

    try:
        # Determine how many characters will be in the password.
        length_of_password = int(input(f'Number of characters for password (>= {REQUIRED_LENGTH_OF_PASSWORD}): '))
    except ValueError:
        print(f'Invalid character entered. Must be a number. Default length is {length_of_password}.')
    
    if length_of_password < REQUIRED_LENGTH_OF_PASSWORD:
        print(f'The length must be at least {REQUIRED_LENGTH_OF_PASSWORD}.\nGenerating a password that is long enough.')

        # Force the length to be at least at long as is required characters.
        length_of_password = REQUIRED_LENGTH_OF_PASSWORD

    for _ in range(length_of_password):
        generated_password += rn.choice(CHARACTERS_FOR_PASSWORD)

    return generated_password


def main():
    print(password_generator())


if __name__ == '__main__':
    main()
