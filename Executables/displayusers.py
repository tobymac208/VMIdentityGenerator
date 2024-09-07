import os
import bcrypt

PASSWORD_FILE = "../Sec/masterpass"

def authenticate():
    '''
        Required step to allow the user to view all of the password information.
    '''
    password_not_set = False
    stored_hash = None

    with open(PASSWORD_FILE, "rb") as f: # Check if the password is empty.
        hashed_pass = f.read()        
    
        if len(hashed_pass) < 1:
            print("The password has not been generated.")
            password_not_set = True
        else: # A hash was found so store it.
            stored_hash = hashed_pass
    
    if password_not_set:
        print("The administrator's password must be set. Exiting program...")

        # TODO: Remove later.
        pwd = input("No password. Please enter master password: ")
        str.encode(pwd)
        salt = bcrypt.gensalt(rounds=15)
        # Hashing the password
        hashed = bcrypt.hashpw(password, salt)

        return -1
    
    # Otherwise, attempt to login with the administrator password.
    password = input("Enter master password: ")
    password = str.encode(password)
    # Adding the salt to password
    salt = bcrypt.gensalt(rounds=15)
    # Hashing the password
    hashed = bcrypt.hashpw(password, salt)

    print(f"{stored_hash} and {hashed}")
    
    if bcrypt.checkpw(stored_hash, hashed):
        print("Authenticated!")
        return 1
    else:
        print(f"Passwords do not match.")
        return -1 # Failed authentication.


def main():
    if authenticate() < 0: # Authenticate before the files are accessed.
        return # exit function

    all_data_concat = ""

    FILE_PATH = "Identities/"
    file_list = os.listdir(FILE_PATH)

    for item in file_list:
        # Attempt to read each file.
        with open(f"{FILE_PATH}{item}", "r") as f:
            print(f"Data found in {item} >>>")
            
            for line in f.readlines():
                if line != "\n":
                    print(line.strip())
            print("")


if __name__ == "__main__":
    main()

