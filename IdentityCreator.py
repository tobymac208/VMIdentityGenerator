import subprocess
from PasswordGenerator import Generate


class Identity:
    # email, first name, last name, password, DOB, PIN
    '''
        Generates a person object.
    '''
    def __init__(self, fName, lName, email, password, dob, pin):
        self.fName = fName
        self.lName = lName
        self.email = email
        self.password = password
        self.dob = dob
        self.pin = pin

    def __str__(self):
        return f"Name: {self.fName} {self.lName} Email: {self.email} DOB {self.dob}"

    def identity_details(self):
        '''
            For use only when printing the data to a file. Simply returns the string of all of the data in the object.
        '''
        return f"Name: {self.fName} {self.lName}\nEmail: {self.email}\nDate of Birth: {self.dob}\nPassword: {self.password}\nPIN: {self.pin}"


def main():
    # Create an account
    firstName = input("first name: ")
    lastName = input("last name: ")
    print(f"Name of {firstName} {lastName} set!")
    
    # Setup a default email, but let them change it.
    email = firstName + "." + lastName + "@outlook.com"
    print(f"Your default email is {email}. Would you like to change this?")
    change_email = input("y/n? ")
    if change_email.upper() == "Y":
        email = input("Please input a new email: ")
    print("Email set!")

    # Generate a password.
    password = Generate.password_generator()
    print("Password set!")
    
    dob = input("date of birth: ")
    print("DOB set!")
    
    # Get a PIN from the user.
    PINFirstAttempt = input("PIN: ")
    PINSecondAttempt = input("Re-enter your PIN: ")
    while PINFirstAttempt != PINSecondAttempt:
        print("The PINs do not match. Please re-enter your PIN!")
        PINFirstAttempt = input("PIN: ")
        PINSecondAttempt = input("Re-enter your PIN: ")
    pin = PINFirstAttempt
    print("PIN Set!")


    # initialize the new object
    account = Identity(firstName, lastName, email, password, dob, pin)
    print("Account created!")

    FILE_PATH = "Identities/"
    FILE_GENERATED_NAME = f"{FILE_PATH}{firstName[0]}{lastName}.txt"

    # Add the identity to a new identity file.
    with open(FILE_GENERATED_NAME, "w+") as f:
        f.write(account.identity_details() + "\n")
    print(f"File generated for identity. File name: {FILE_GENERATED_NAME}")


if __name__ == "__main__":
    main()
