import time
from git.repo import Repo
import Utils.GeneralUtils as gu

repositoriesDict = []

def GitSync():

    repositoriesDict = gu.ReadPreferences()

    for repositoryPrefs in repositoriesDict:
        if repositoryPrefs["active"] == False:
            continue
        print(f'Syncing Repository: {repositoryPrefs["name"]}')
        currentTime = time.strftime("%H:%M:%S")
        print("GitSync function is running at " + currentTime)
        # GetListOfModifiedFiles(repositoryPrefs["repo_dir"])
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
    try:
        repo = Repo(RepoDirectory)
    except:
        print("Repository is not initialized")
        repo = Repo.init(RepoDirectory)
        print("Repository is initialized")

    files_to_commit = GetListOfCommitFiles(RepoDirectory)

    if repo.untracked_files:
        repo.git.add(all=True)
    
    if repo.is_dirty():
        print("There are changes in the repository, will commit the following files:")
        print(files_to_commit["new"])
        print(files_to_commit["modified"])
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

def GetListOfCommitFiles(RepoDirectory):
    repository = Repo(RepoDirectory)
    message_modified_files = "Modified files: "
    message_new_files = "New files: "

    modified_files = repository.index.diff(None)
    if modified_files:
        for file in modified_files:
            message_modified_files += GetFileName(file.a_path) + ", "
    else:
        message_modified_files += " none, "
    
    new_files = repository.untracked_files
    if new_files:
        for file in new_files:
            message_new_files += GetFileName(file) + ", "
    else:
        message_new_files += " none, "
    # create an empty dictionary
    committed_files = {}
    # add new files to the dictionary
    committed_files["new"] = message_new_files[:-2]
    # add modified files to the dictionary
    committed_files["modified"] = message_modified_files[:-2]
    return committed_files

    
def GetFileName(path):
    lastSlash = path.rfind("/")
    fileName = path[lastSlash + 1:]
    return fileName