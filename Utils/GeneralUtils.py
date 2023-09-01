import os
import json
from dotenv import load_dotenv

load_dotenv()

# Get the value of the ENV variable
env = os.getenv('ENV')
 
def ReadPreferences():

    if env == 'Development':
        json_file_path = 'preferences.dev.json'
    
    if env == 'Testing':
        json_file_path = 'preferences.testing.json'
    
    if env == 'Production':
        json_file_path = 'preferences.json'
    
    prefDict = []
    try:
        with open(json_file_path) as preferences:
            data = json.load(preferences)

        for repository in data["repositories"]:
            prefDict.append(repository)
    except Exception as e:
        print("Error reading the preferences file")
        print("Please make sure the file exists and is in the correct format: " + json_file_path)
        print("Exception: " + str(e))
        quit()
    return prefDict

def ReadApplicationSettings():
    if env == 'Development':
        json_file_path = 'preferences.dev.json'
    
    if env == 'Testing':
        json_file_path = 'preferences.testing.json'
    
    if env == 'Production':
        json_file_path = 'preferences.json'
        
    appSettings = {}
    try:
        with open(json_file_path) as preferences:
            data = json.load(preferences)

        for setting in data["app"]:
            appSettings[setting] = data["app"][setting]
    except Exception as e:
        print("Error reading the app settings file")
        print("Please make sure the file exists and is in the correct format: " + json_file_path)
        # print the exception error message
        print("Exception: " + str(e))
        quit()
    return appSettings