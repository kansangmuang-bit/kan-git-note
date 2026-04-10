

## What is Git?

Git is version control software. Git is local to your machine. Github is a remote place for a git repo to live.

## Basic Commands

`git init` - creates the .git folder. it initializes the git repository

To remove an initialized repo, we can run `rm -rf .git` (or more safely, place the .git folder in the recycle bin)

`git add [filename] [filename] [...]` - stages files for the next commit

`git add .` - stages all the files in the current directory

`git commit -m "some message"` - makes the snapshot/saves the current state of the project

`git status` - tells us information such as 

- the branch we are on

- files that have been staged

- files that have been modified since the last commit

- and more

`git branch [branch-name]` - creates a branch

`git checkout [branch-name]` - switches to the branch

`git switch [branch-name]` - also switches to the branch indicated

`git clone [url-for-project]` - downloads a remote repo (ex: from github)

`git push [remote-name] [branch-name]` - takes local commits and uploads them the remote repo on the indicated branch 
(ex: `git push origin main`)

`git pull [remote-name] [branch-name]` - takes remotes commits and downloads them to update the local repo.
(ex: `git pull origin main`)

## Other Tools and Vocab

**pull request** - a Github feature that allows for an easier time with merging. 

**gitbash** - a bash-like shell that we downloaded with git. We also added it to windows terminal. 

**Github CLI** - Github Command Line Interface is a command line tool to interact with github on your machine. Can be useful when handling authentication on the Raspberry Pi. Run `gh auth login` to login to it via command line.

**Github Desktop** - a gui application for git.

**Git Flow** - a basic branching strategy for managing git repos.
https://nvie.com/posts/a-successful-git-branching-model/

## Other Notes

- It is a good idea to NOT push to main

- It is a good idea to put someone in charge of processing pull requests.
