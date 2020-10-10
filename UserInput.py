from CSVUtility import CSV_Util

class UserInputs():

    login_data = CSV_Util()
    choice = ""
    username = ""
    password = ""

    def __init__(self):
        a = 1

    def initial_prompt(self):
        print("If you would like to login using existing credentials, type '1'. \nIf you would like to create a new "
              "user, type '2'.")
        self.choice = input("1 or 2: ")
        while self.choice != "1" and self.choice != "2":
            self.choice = input("Unrecognized input, please type '1' to login or '2' to create a new user: ")
        print("---"*15)
        return self.choice

    def prompt_existing_user(self):
        print("Please enter your credentials:")
        self.username = input("Username: ")
        self.password = input("Password: ")

