# GitSync

This is a utility to sync repositories like note taking apps like Obsidian to Github, and other repositories for non production use.

## Requirements

Use `pip3 install -r requirements.txt` to install the requirements.

### Libraries used:

- gitPython

### Modules used:

- schedule
- dotenv

### Requirements

Install the required libraries:

```bash
pip install -r requirements.txt
```

### How to use

##### Set preferences

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
  "app": 
    {
      "job_schedule": "minute",
      "job_schedule_factor": 1
    }
}
```

#### Run the script

```python
python3 gitSync.py
```
