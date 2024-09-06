from PasswordGenerator import Generate
from os.path import exists
import os
from time import sleep


def pause_and_notify(time, message):
    '''
        Waits a certain amount of time with an informative message.
    '''
    print(message)
    sleep(time)


class Identity:
    # email, first name, last name, password, DOB, PIN
    '''
        Generates a person object.
    '''
    def __init__(self):
        print("You'd like to create a new identity? Well, here we go. Please provide the following information.")

        self.fName, self.lName = self.get_name()
        self.email = self.get_email()
        self.password = self.get_password()
        self.dob = self.get_dob()
        self.pin = self.get_pin()

        print(self.identity_details())
    
    def get_name(self) -> tuple:
        firstName = input("first name: ")
        lastName = input("last name: ")
        
        return (firstName, lastName)
    
    def get_email(self) -> str:
        # Setup a default email, but let them change it.
        email = self.fName + "." + self.lName + "@outlook.com"
        print(f"Your default email is {email}. Would like to keep this?")
        change_email = input("y/n? ")
        if change_email.upper() == "N":
            email = input("Please input a new email: ")

        return email
    
    def get_password(self) -> str:
        # Generate a password.
        password = Generate.create_phrase_password()
        print("The password has been generated and can be found in the file.")
        
        return password
    
    def get_dob(self) -> str:
        dob = input("date of birth: ")

        return dob
    
    def get_pin(self) -> str:
        # Get a PIN from the user.
        PINFirstAttempt = input("PIN: ")
        PINSecondAttempt = input("Re-enter your PIN: ")
        while PINFirstAttempt != PINSecondAttempt:
            print("The PINs do not match. Please re-enter your PIN!")
            PINFirstAttempt = input("PIN: ")
            PINSecondAttempt = input("Re-enter your PIN: ")
        
        pin = PINFirstAttempt
        
        return pin

    def __str__(self):
        return f"Name: {self.fName} {self.lName}\nEmail: {self.email}\nDate of Birth: {self.dob}\nPassword: {self.password}\nPIN: {self.pin}"

    def identity_details(self):
        '''
            Note: For use only when printing the data to a file. Simply returns the string of all of the data in the object.
        '''
        return f"Name: {self.fName} {self.lName}\nEmail: {self.email}\nDate of Birth: {self.dob}\nPassword: {self.password}\nPIN: {self.pin}"


def helper_write_it(filename, ident):
    '''
        Add the identity to a new identity file.
    '''
    with open(filename, "w+") as f:
        f.write(ident.identity_details() + "\n")
        print(f"File generated for identity. File name: {filename}")

def write_data_to_file(ident) -> bool:
    # give all identities to the user
    FILE_PATH = "Identities/"

    FILE_GENERATED_NAME = f"{FILE_PATH}{ident.fName}{ident.lName}.txt"

    if(exists(FILE_GENERATED_NAME)): # A file with that name exists.
        print(f"{FILE_GENERATED_NAME} already exists. This file cannot be created.\nDo you want to clobber the previous file? (y/n)")

        is_clobberable = input(">> ").lower()

        # Ensure the user wants to clobber the file.
        if is_clobberable == "y" or is_clobberable == "yes":
            helper_write_it(FILE_GENERATED_NAME, ident)

            pause_and_notify(5, "The data has been clobbered. Returning to menu...")
        else:
            pause_and_notify(5, "Not clobbering data. Keeping the original file intact. Returning to menu...")
            
    else:
        helper_write_it(FILE_GENERATED_NAME, ident)


def menu():
    options = [
        'Exit',
        'Create an identity'
    ]

    while True:
        if len(options) < 1:
            print('No menu options are available.')
            return -1 # Exit function with the exit code.
        print("Menu options:")
        for i in range(len(options)): print(f'{i}: {options[i]}')

        user_input = int(input("Enter your choice >> ").strip())

        if user_input == 1:
            #Create a new identity
            new_user = Identity()
            write_data_to_file(new_user)

        elif user_input == 0: # Exit the loop
            return 0
        else: print("Invalid character. Ignoring input.")

        os.system('cls' if os.name == 'nt' else 'clear') # Always clear the screen at the end.


def main():
    return_code = menu()
    print(f"Menu returned with code. {return_code}")


if __name__ == "__main__":
    main()

    print("Everything is done. Exiting program...")
