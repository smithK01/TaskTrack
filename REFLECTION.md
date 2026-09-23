# ICA04 Reflection

## 1. Local and Remote Repositories

What is the difference between the local TaskTrack repository and the repository hosted on GitHub?

- The difference between the local repository and the repository hosted on GitHub is just where it is stored, and what version the repo is. For example, the local repository is stored locally on my laptop, where as the repository hosted on GitHub is obviously on GitHub's servers. I make changes to the local repo without diruption the online one, and when happy with the changes I push those local changes to the online repo.

## 2. Connecting and Pushing

Why did adding `origin` not immediately place the project files on GitHub?

- Because we needed to push the actually files for the repository. I need to upload the local repo in order for it to exist on GitHub.

## 3. Cloning

How is cloning a repository different from downloading its files as a ZIP archive?

- downloading the files as a zip archive only gives you the project files, no .git files, and no version history. Cloning a repository gives you all of that, and lets you use the git remote command to point towards origin, the original repo.

## 4. Fetching and Pulling

What information did `git fetch` update, and what additional action did `git pull` perform?

- git fetch gets all the commits from the origin on GitHub, and updates tracking to show you how the local repo is different without actually changing the local repo. git pull does the same thing, but actually changes the local repo files to match the remote one.

## 5. Focused Commits

Why is it useful to commit the Python feature, sample task data, and README documentation separately?

- Because by only making one commit to the repo at a time, we can have an easier time rolling back if something is wrong, and it makes it easier to see what's changed and why.