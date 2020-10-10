from CSVUtility import CSV_Util
from UserInput import UserInputs

login_data = CSV_Util()
user = UserInputs()


# Run logic -- possibly break out to new class
user.initial_prompt()

if user.choice == "1":
    # Login using existing credential
    login_success = False
    while not login_success:
        user.prompt_existing_user()
        if user.existing_user_login_flow(user.username, user.password):
            login_success = True
            user.login_success()
elif user.choice == "2":
    # Create new user flow
    user.prompt_new_username()
    user.prompt_new_password()
    login_data.add_new_user(user.new_username, user.new_password)

login_data.update_csv()


