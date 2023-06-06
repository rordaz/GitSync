import os
import json
from dotenv import load_dotenv

load_dotenv()

# Get the value of the ENV variable
env = os.getenv('ENV')
 
def ReadPreferences():

    if env == 'development':
        json_file_path = 'preferences.dev.json'
    else:
        json_file_path = 'preferences.json'
    prefDict = []
    try:
        with open(json_file_path) as preferences:
            data = json.load(preferences)

        for repository in data["repositories"]:
            prefDict.append(repository)
    except:
        print("Error reading the preferences file")
        quit()
    return prefDict
