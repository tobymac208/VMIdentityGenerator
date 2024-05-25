import os


def main():
    all_data_concat = ""

    FILE_PATH = "../Identities/"
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

