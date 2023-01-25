import json

# create a function to read user preferences from a json file
def ReadPreferences():

    prefDict = []
    
    try:
        with open('preferences.json') as preferences:
            data = json.load(preferences)

        for repository in data["repositories"]:
            prefDict.append(repository)
    except:
        print("Error reading the preferences file")
        quit()
    return prefDict
