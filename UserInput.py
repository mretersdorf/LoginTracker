from UtilCSV import CSV_Util

class UserInputs():

    logins = CSV_Util()
    username = ""
    password = ""

    def __init__(self):
        a = 1

    def prompt_user_inputs(self):
        print("Please enter your credentials:")
        self.username = input("Username: ")
        self.password = input("Password: ")

    def login_flow(self):
        if self.logins.check_credentials(self.username, self.password):
            print("!!!! ---- Username exists ---- !!!!")
            if self.logins.password_match:
                print("*" * 10 + "Login Successful. Welcome!" + "*" * 10)
            else:
                change_password = input("Password does not match. Would you like to change it? Y/N  - ")
                if change_password.lower() == "y":
                    print("Please Change your password:")
                elif change_password.lower() == "n":
                    print("You selected No. Goodbye!")
                else:
                    print("Input not recognized. Goodbye!")