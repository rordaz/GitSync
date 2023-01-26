import time
from git.repo import Repo
import Utils.GeneralUtils as gu

repositoriesDict = []

def GitSync():

    repositoriesDict = gu.ReadPreferences()

    for repositoryPrefs in repositoriesDict:
        print(f'Syncing Repository: {repositoryPrefs["name"]}')
        SyncRepo(repositoryPrefs)
        time.sleep(1)

def SyncPush(repo):
    
    branch = repo.active_branch
    
    remote_branch = branch.tracking_branch()
    
    try:
        if branch.commit != remote_branch.commit:
            if branch.commit.hexsha == remote_branch.commit.hexsha:
                print("Local and remote branches are in sync, no need to push.")
                return
            else:
                repo.git.push()
                print(f"Pushed changes to {remote_branch}.")
        else:
            print("Local and remote branches are in sync, no need to push.")
    except Exception as e:
        print("Error while pushing changes to remote repository:", e)
        return

def SyncRepo(repoPrefs):

    RepoDirectory = repoPrefs["repo_dir"]
    currentTime = time.strftime("%H:%M:%S")

    print("SyncRepo function is running at " + currentTime)
    try:
        repo = Repo(RepoDirectory)
    except:
        print("Repository is not initialized")
        repo = Repo.init(RepoDirectory)
        print("Repository is initialized")

    if repo.untracked_files:
        repo.git.add(all=True)

    if repo.is_dirty():
        print("There are changes in the repository, will commit")
        commitMessage = GetCommitMessage(repoPrefs["auto_commit_message"])
        repo.git.add(all=True)
        repo.git.commit(m=commitMessage)
    else:
        print("There are no changes in the local repository to commit")
    
    # Check Remote Changes
    SyncRemote(RepoDirectory)
    print("Syncronization was completed on " + time.strftime("%m-%d-%Y %H:%M:%S"))
    print("--------------------------------------------------")

def SyncRemote(RepoDirectory):
    
    try:
        repo = Repo(RepoDirectory)
    except:
        print("Repository is not initialized, please initialize the repository. Syncronization will not be completed")
        return

    if repo.remotes:
        print("Contacting remote repository...")
        try:
            repo.git.pull()
            SyncPush(repo)
        except:
            print("The remote repository can't be reach. Check your connection. Syncronization will not be completed")
            print("Hint: git remote add origin [repo url]")
            return
    else:
        print("There is no remote repository, please add a remote. Syncronization will not be completed")
        print("Hint: git remote add origin [repo url]")
        return

def GetCommitMessage(commitMessage):
    return  commitMessage + time.strftime(" %m%d%Y_%H%M%S")