import schedule
import time
import Utils.GitUtils as gt
import Utils.GeneralUtils as gu
from git import Repo

# Path to the local repository
#gitDir = r"C:\Users\H508391\source\repos\TestRepo"

# Run the SyncRepo function once at the start of the program
#gt.SyncRepo(gitDir)

print("GitSync is running")
gt.GitSync()

# Schedule the SyncRepo function to run every 5 minutes
schedule.every(5).minutes.do(gt.GitSync)

while True:
    schedule.run_pending()
    time.sleep(1)
