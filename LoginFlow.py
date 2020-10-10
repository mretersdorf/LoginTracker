from CSVUtility import CSV_Util
from UserInput import UserInputs

login_data = CSV_Util()
user = UserInputs()


def existing_user_login_flow(username, password):
    if login_data.check_credentials(username, password):
        print("!!!! ---- Username exists ---- !!!!")
        if login_data.password_match:
            print("*" * 10 + "Login Successful. Welcome!" + "*" * 10)
            return True
        else:
            print("Password does not match. Please re-enter your credentials")
            return False


# Run logic

user.initial_prompt()
if user.choice == "1":
    # Login using existing credential
    user.prompt_existing_user()
    while existing_user_login_flow(user.username, user.password) == False:
        user.prompt_existing_user()
