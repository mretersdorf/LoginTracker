import csv

class CSV_Util():

    f = open("LoginData.csv")
    logins = csv.DictReader(f)
    username_match = False
    password_match = False
    user_row = 0

    def __init__(self):
        a = "abc"

    def check_credentials(self, username, password):
        row_num = 0
        for row in self.logins:
            print(row['name'], row['password'])
            if username.lower() == row['name'].lower():
                self.username_match = True
                self.user_row = row_num
                self.check_password(password, row['password'])
                return True
            else:
                print("username does not match \n")
            row_num = row_num + 1

    def check_password(self, user_password, login_password):
        if user_password == login_password:
            self.password_match = True
        else:
            self.password_match = False

    def add_new_user(self, username, password):


