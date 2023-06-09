import schedule
import time
from Types.Schedule import Periodicity
import Utils.GitUtils as gt
import Utils.GeneralUtils as gu
from git.repo import Repo

print("GitSync is running")
repositoriesDict = gu.ReadPreferences()
applicationSettings = gu.ReadApplicationSettings()
gt.GitSync(repositoriesDict)

if applicationSettings["job_schedule_frequency"] == Periodicity.MINUTE.value:
    schedule.every(applicationSettings["job_schedule_factor"]).minutes.do(
        gt.GitSync, repositoriesDict)
elif applicationSettings["job_schedule_frequency"] == Periodicity.HOURLY.value:
    schedule.every(applicationSettings["job_schedule_factor"]).hours.do(
        gt.GitSync, repositoriesDict)
elif applicationSettings["job_schedule_frequency"] == Periodicity.DAILY.value:
    schedule.every(applicationSettings["job_schedule_factor"]).days.do(
        gt.GitSync, repositoriesDict)

while True:
    schedule.run_pending()
    time.sleep(1)
