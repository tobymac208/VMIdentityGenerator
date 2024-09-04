from PasswordGenerator import Generate


class Identity:
    # email, first name, last name, password, DOB, PIN
    '''
        Generates a person object.
    '''
    def __init__(self):
        print("You'd like to create a new identity? Well, here we go. Please provide the following information.")

        self.fname, self.lName = self.get_name()
        self.email = self.get_email()
        self.password = self.get_password()
        self.dob = self.get_dob()
        self.pin = self.get_pin()
    
    def get_name(self) -> tuple:
        firstName = input("first name: ")
        lastName = input("last name: ")
        
        return (fName, lName)
    
    def get_email(self) -> str:
        # Setup a default email, but let them change it.
        email = firstName + "." + lastName + "@outlook.com"
        print(f"Your default email is {email}. Would you like to change this?")
        change_email = input("y/n? ")
        if change_email.upper() == "Y":
            email = input("Please input a new email: ")

        return email
    
    def get_password(self) -> str:
        # Generate a password.
        password = Generate.create_long_password()
        
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
        return f"Name: {self.fName} {self.lName} Email: {self.email} DOB {self.dob}"

    def identity_details(self):
        '''
            Note: For use only when printing the data to a file. Simply returns the string of all of the data in the object.
        '''
        return f"Name: {self.fName} {self.lName}\nEmail: {self.email}\nDate of Birth: {self.dob}\nPassword: {self.password}\nPIN: {self.pin}"


def menu():
    '''
    '''
    options = [
        'Create an identity'
    ]

    while True:
        if len(options) < 1:
            print('No menu options are available.')
            return -1 # Exit function with the exit code.

        for i in range(len(options)):
            print(f'{i+1} {options[i]}')

        user_input = int(input("Enter your choice >> ").strip())

        if user_input == 1:
            #Create a new identity 
            new_user = Identity()


def main():
    return_code = menu()
    print(f"Menu returned with code. {return_code}")


if __name__ == "__main__":
    main()


# TODO: Re-integrate this code again. This code deals with the 

'''
FILE_PATH = "Identities/"
    FILE_GENERATED_NAME = f"{FILE_PATH}{firstName[0]}{lastName}.txt"

    # Add the identity to a new identity file.
    with open(FILE_GENERATED_NAME, "w+") as f:
        f.write(account.identity_details() + "\n")
    print(f"File generated for identity. File name: {FILE_GENERATED_NAME}")

'''