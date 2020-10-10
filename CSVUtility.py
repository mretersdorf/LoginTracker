import csv

class CSV_Util():

    login_data = {}
    username_match = False
    password_match = False
    user_row = 0

    def __init__(self):
        f = open("LoginData.csv")
        csv_data = csv.DictReader(f)
        for row in csv_data:
            self.login_data[row['name']] = row['password']
        f.close()

    def check_credentials(self, username, password):
        if username in self.login_data:
            self.username_match = True
            if self.login_data[username] == password:
                print("Password Matches! Login Successful!")
                self.password_match = True
            else:
                print("Password does not match")
                self.password_match = False
        else:
            print("Username does not match")
            self.username_match = False

    def check_username(self, username):
        if username in self.login_data:
            return True
        else:
            return False

    def check_password(self, username, password):
        if self.login_data[username] == password:
            return True
        else:
            return False

    def add_new_user(self, username, password):
        self.login_data[username] = password

    def update_csv(self):
        with open('LoginData.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'password']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for key in self.login_data:
                writer.writerow({'name': key, 'password': self.login_data[key]})
        csvfile.close()




