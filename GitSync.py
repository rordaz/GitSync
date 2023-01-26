import schedule
import time
import Utils.GitUtils as gt
import Utils.GeneralUtils as gu
from git.repo import Repo

print("GitSync is running")
gt.GitSync()

# Schedule the SyncRepo function to run every 5 minutes
# todo: make this configurable
schedule.every(5).minutes.do(gt.GitSync)

while True:
    schedule.run_pending()
    time.sleep(1)
