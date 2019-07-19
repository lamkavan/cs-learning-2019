"""
Solutions

Question 1
Git is a tool that developers can use to help organise their code and also make
it easier for multiple developers to collaborate on the same project. Git has many
features that make the development and maintaining of large projects easier.
Fundamentally, Git is a tool that allows you to store you code remotely (kind of like Dropbox)

Question 2
A repository is like a folder that holds all the file and content for a specific project.
You can create a repo by going to Github and creating a repo under your account.
You can even do it via terminal by using the git init command (not mentioned in class)

Question 3
You can make a git ignore file and simply add the files or file types to the git ignore file.
Then when you do git status (for example) you will no longer see it listed.

Question 4
First make a gitignore file. Then open the empty file and add two lines.
__________
hello.txt
*.js
__________

Question 5
When you have multiple people working on the same file at the same time you can have
merge conflicts. To avoid these conflicts you could communicate with you team and organise
your development such that only one person works on the file at a time.

Question 6
You will create the repo then do git clone <repo url>. After making the file and editing it
you should do git add <file_name> then git commit -m"<your_message>". Finally do git push origin master

Question 7
One easy way to do this is just to use git pull. That fetches and merges the changes your friend made.

Question 8
"""