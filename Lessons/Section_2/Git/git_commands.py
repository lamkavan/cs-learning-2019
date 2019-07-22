"""
The following is a summary of all the git commands that we discussed in class

1) git clone <repo_URL>
This command downloads and puts a local copy of the repo specified by the
repo URL (get the url by visiting the repo on Github website). Changes made to
your local copy will not be reflected onto the remote copy until you push.

2) git status
Use this command within a repo to see the status of your repo. It will display the
branch you are on. In addition it will list (in red) files that have been modified,
deleted, moved and new files that have been added to the repo. You will need to use git
add in order to stage the files for a commit (add file to the present box). Once added
to the "present box" the file(s) will appear green indicating they are staged for a commit.

3) git add <file_name>
This command stages a file for a commit (adds the file to the present box).

4) git commit -m"<your message>"
This command commits all staged files you added using git add. In otherwords, wrap
up the present box and write a message on the box.

5) git push <the original place of repo> <branch>
Usually you will see this used as git push origin master. Origin is just something that
git knows as the location of the original repo (the remote version of repo that you
clone from). Master is the branch you want to push to. Pushing is basically like sending
the present box.

6) git pull
This command is issued within a repo and basically updates your local version to match
the remote version. Make sure you do this before doing any new work on the repo.

There are many more commands for git, but these are the basic ones that you should know
as a young programmer and computer scientist.
"""