import pandas
import csv
from UtilCSV import CSV_Util
from UserInput import UserInputs

#prompt user for user name password
    #Ask user to login or create new entry

    #Login
        #Ask for username/password
        #Check CSV for existing
            #IF name is recognized but password is incorrect, fail
            #IF name is not recorgnized, fail and bring user into new entry flow
            #IF name is recognized and password matches, then LOGIN (SUCCESS)

    #Create New Entry
        #Prompt user for new user name and 2 matching passwords
            #IF user name does not exist:
                #IF passwords do no match
                    #Tell user passwords do not match and to try again
                #IF passwords do match
                    #Create new entry in csv
            #IF username does exist:
                #Apend to CSV file
                #Prompt user to login
logins = CSV_Util()
user = UserInputs()

#Run logic
user.prompt_user_inputs()
user.login_flow()

