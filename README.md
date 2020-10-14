# LoginTracker

## Description
Prompts a user to enter login information (username / password)  
Login data is stored in a file LoginData.csv  

### Workflow
Prompt the user to create a new login or log in using existing credentials

**Login using existing credentials:**  
* If the login username / password matches, then log the user in.  
* If the login username does not match, then explain username not found an give the user the initial prompt
* If the login username matches, but the password does not match, then explain that the password does not match and give the user the initial prompt

**Create new user:**  
Prompt user to enter username 
* If user name exists, explain that username already exists and give the user the initial prompt
* If user name does not exist, prompt user to enter a password   

Prompt user to enter a password
* Login credentials are stored in LoginData.csv
 
