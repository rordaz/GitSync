import time
from git import Repo, GitCommandError
import Utils.GeneralUtils as gu


# create a dictionary to store the repositories from the preferences file
repositoriesDict = []

def GitSync():

    #read the program preferences
    repositoriesDict = gu.ReadPreferences()

    for repo in repositoriesDict:
        SyncRepo(repo["repo_dir"])
        time.sleep(1)

def SyncPush(repo):
    
    # Get the current branch
    branch = repo.active_branch
    
    # Get the remote tracking branch for the current branch
    remote_branch = branch.tracking_branch()
    
    try:
        # Compare the local and remote branches
        if branch.commit != remote_branch.commit:
            if branch.commit.hexsha == remote_branch.commit.hexsha:
                print("Local and remote branches are in sync, no need to push.")
                return
            if branch.commit > remote_branch.commit:
                # Local branch is ahead of remote branch, so push the changes
                repo.git.push()
                print(f"Pushed changes to {remote_branch}.")
        else:
            print("Local and remote branches are in sync, no need to push.")
    except Exception as e:
        print("Error while pushing changes to remote repository:", e)
        return

def SyncRepo(RepoDirectory):

    # get current time and date
    currentTime = time.strftime("%H:%M:%S")

    print("SyncRepo function is running at " + currentTime)
    # Create a new repository object and handle the exception if the repository is not initialized
    try:
        repo = Repo(RepoDirectory)
    except:
        print("Repository is not initialized")
        repo = Repo.init(RepoDirectory)
        print("Repository is initialized")

    # check if there are untracked files
    if repo.untracked_files:
        # print("There are untracked files")
        # print the list of untracked files
        # print(repo.untracked_files)
        # add new files to the index
        repo.git.add(all=True)
    # else:
    #     print("There are no untracked files")


    # if there are changes in the repository then add them to the index, them commit them
    if repo.is_dirty():
        print("There are changes in the repository, will commit")
        commitMessage = GetCommitMessage()
        # add the tracked files to the index
        repo.git.add(all=True)
        # add new files to the index
        repo.git.commit(m=commitMessage)
    else:
        print("There are no changes in the local repository to commit")
    
    # Check Remote Changes
    SyncRemote(RepoDirectory)
    print("Syncronization was completed on " + time.strftime("%m-%d-%Y %H:%M:%S"))
    print("--------------------------------------------------")

#create a function that check if there is remote repository and if there is one then push the changes to the remote repository
def SyncRemote(RepoDirectory):
    
    # Create a new repository object and handle the exception if the repository is not initialized
    try:
        repo = Repo(RepoDirectory)
    except:
        print("Repository is not initialized, please initialize the repository. Syncronization will not be completed")
        return


    # check if there is a remote repository
    if repo.remotes:
        print("Contacting remote repository...")
        # pull the changes from the remote repository, catch the exception if there is no remote repository
        try:
            repo.git.pull()
            # push if there is local changes
            SyncPush(repo)
        except:
            print("The remote repository can't be reach. Check your connection. Syncronization will not be completed")
            print("Hint: git remote add origin [repo url]")
            return
    else:
        print("There is no remote repository, please add a remote. Syncronization will not be completed")
        print("Hint: git remote add origin [repo url]")
        return

# create a function that outputs the current time and date to string with the format "DDMMYYYY_HHMMSS"
def GetCommitMessage():
    return "Auto Commit by GitSync " + time.strftime("%m%d%Y_%H%M%S") + "_W"