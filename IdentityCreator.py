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


FILE_PATH = "Identities/"

def main():
    # Create an account
    firstName = input("first name: ")
    lastName = input("last name: ")
    email = firstName + "." + lastName + "@outlook.com"
    password = input("password: ")
    dob = input("date of birth: ")
    pin = input("PIN: ")
    # initialize the new object
    account = Identity(firstName, lastName, email, password, dob, pin)

    # Add the identity to a new identity file.
    with open(f"{FILE_PATH}{firstName[0]}{lastName}.txt", "w+") as f:
        f.write(account.identity_details() + "\n")


main()
