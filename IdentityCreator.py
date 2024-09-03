from PasswordGenerator import Generate


class Identity:
    # email, first name, last name, password, DOB, PIN
    '''
        Generates a person object.
    '''
    def __init__(self, fName, lName, email, password, dob, pin):
        fullName = self.get_name().split()
        self.fName = fullName[0]
        self.lName = fullName[1]
        self.email = self.get_email()
        self.password = self.get_password()
        self.dob = self.get_dob()
        self.pin = self.get_pin()
    
    def get_name(self):
        firstName = input("first name: ")
        lastName = input("last name: ")

        self.fName = firstName
        self.lName = lastName
        print(f"Name of {firstName} {lastName} set!")
    
    def get_email(self):
        # Setup a default email, but let them change it.
        email = firstName + "." + lastName + "@outlook.com"
        print(f"Your default email is {email}. Would you like to change this?")
        change_email = input("y/n? ")
        if change_email.upper() == "Y":
            email = input("Please input a new email: ")
        
        self.email = email
        print("Email set!")
    
    def get_password(self):
        # Generate a password.
        password = Generate.create_long_password()
        
        self.password = password
        print("Password set!")
    
    def get_dob(self):
        dob = input("date of birth: ")
        
        self.dob = dob
        print("DOB set!")
    
    def get_pin(self):
        # Get a PIN from the user.
        PINFirstAttempt = input("PIN: ")
        PINSecondAttempt = input("Re-enter your PIN: ")
        while PINFirstAttempt != PINSecondAttempt:
            print("The PINs do not match. Please re-enter your PIN!")
            PINFirstAttempt = input("PIN: ")
            PINSecondAttempt = input("Re-enter your PIN: ")
        
        pin = PINFirstAttempt
        
        self.pin = pin
        print("PIN Set!")

    def __str__(self):
        return f"Name: {self.fName} {self.lName} Email: {self.email} DOB {self.dob}"

    def identity_details(self):
        '''
            For use only when printing the data to a file. Simply returns the string of all of the data in the object.
        '''
        return f"Name: {self.fName} {self.lName}\nEmail: {self.email}\nDate of Birth: {self.dob}\nPassword: {self.password}\nPIN: {self.pin}"


def main():
    FILE_PATH = "Identities/"
    FILE_GENERATED_NAME = f"{FILE_PATH}{firstName[0]}{lastName}.txt"

    # Add the identity to a new identity file.
    with open(FILE_GENERATED_NAME, "w+") as f:
        f.write(account.identity_details() + "\n")
    print(f"File generated for identity. File name: {FILE_GENERATED_NAME}")


if __name__ == "__main__":
    main()
