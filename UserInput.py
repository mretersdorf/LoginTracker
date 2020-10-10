from CSVUtility import CSV_Util

class UserInputs():

    login_data = CSV_Util()
    choice = ""
    username = False
    password = False
    new_username = ""
    new_password = ""

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

    def prompt_new_username(self):
        self.new_username = input("Please enter a new user name: ")
        while self.login_data.check_username(self.new_username):
            self.new_username = input("That username already exists, please enter a new username: ")

    def prompt_new_password(self):
        first_password = input("Please enter your password: ")
        second_password = input("Please re-enter your password: ")
        if first_password == second_password:
            self.new_password = first_password
        else:
            print("Passwords do not match.")
            self.prompt_new_password()

    def prompt_existing_user(self):
        print("Please enter your credentials:")
        self.prompt_username()
        if self.username == False:
            print("The username you entered is not recognized")
            self.prompt_existing_user()
        else:
            self.password = input("Password: ")

    def prompt_username(self):
        prompted_name = input("Username: ")
        if self.login_data.check_username(prompted_name):
            self.username = prompted_name
        else:
            self.username = False
            return False

    def existing_user_login_flow(self, username, password):
        if self.login_data.check_username(username):
            if self.login_data.check_password(username, password):
                return True
            else:
                print("Password does not match. Please re-enter your credentials")
                return False
        else:
            print("That username does not exist.")
            return False

    def login_success(self):
        print("---" * 10 + "Login Successful! Welcome!" + "---" * 10)

