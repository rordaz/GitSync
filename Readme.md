## GitSync

This is a utility to sync repositories like note taking apps like Obsidian to Github, and other repositories for non production use.

You will need to create a Github Personal Access Token with the following permissions:

### Libraries and Modules used in this project:

- gitPython
- schedule
- dotenv

### Installing the Requirements

1. Install Python > 3.10 (https://www.python.org/downloads/)
2. Install Git (https://git-scm.com/downloads)
3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Restart VSCode after installing the requirements.
5. Open GitSync.py and verify that the imports are resolved.

### How to use

#### Set preferences

```json
{
  "repositories": [
    {
      "name": "Repo Name",
      "description": "Description of the repo",
      "repo_dir": "/path/to/repo",
      "created_at": "2022-01-01T12:00:00Z",
      "last_push_at": "2022-01-02T15:30:00Z",
      "language": "Language of the repo",
      "private": true,
      "auto_commit_message": "Auto Commit by GitSync (W)",
      "active": true
    }
  ],
  "app": {
    "job_schedule": "minute",
    "job_schedule_factor": 1
  }
}
```

### Initializing your Obsidian Git Repository

This assumes that you have an Obsidian Vault that you want to sync to Github.

**Steps:**

1. Create a new repository on Github that you want to sync your Obsidian Vault to.
2. Go to the root of your Obsidian Vault
3. Right click in a empty space and select **Open Git Bash here**
4. Run the following commands:

```bash
git init
git add .
```
5. Create a .gitignore file in the root of your Obsidian Vault and add the following:

```gitignore

# MacOS specific files
.DS_Store

# Obsidian Notes Folder you want to ignore
THIS_FOLDER_IS_IGNORED/

# Obsidian Vault Settings
.obsidian/workspace.json
```
6. Commit your changes and push to Github

```bash
git commit -m "Initial Commit"
git branch -M main
git remote add origin https://github.com/USER_NAME/REPO_NAME.git
git push -u origin main
```

#### Run the script

```python
python3 gitSync.py
```
