'''
Question 1  OK
Explain in your own words what Git is and how it can be useful.

Git is a software that allows you to track any changes made in code.
It handles projects and allows multiple people to collaborate on a single file.


Question 2  OK
Explain what a repository is. How do you create a repository.

A repository is like a folder. It is a single large folder that stores multiple files/projects within it.


Question 3  GOOD
If there is a specific file or file types that you want Git to ignore what can you do?

You can make an empty named file with the extension .gitignore and within the file type the names of
the files you want to be ignored. From then on thsose files should not appear.


Question 4  GOOD
When you do "git status" in your repo you see hello.txt, yo.txt and world.js
If you wanted Git to ignore the hello.txt file and all .js files what will you do?

You will go into the .gitignore file and add *.txt and *.js to the list. Any files with that extension,
will automatically be ignored.


Question 5  GOOD
What can happen when you have multiple people working on the same file at the same time?
What is one way you can avoid this?

When multiple people work on a single file they can be changing and altering the same thing, this will confuse git
and make it not know which version to implement.To fix this, talk to the other members of the group to figure out
which version is correct and will be further used. You could always first do git pull and see the updated changes and then go
on with editing them.



Question 6  GOOD
Create a new repository under you Github account called "Summer Project 2019". You can do this
directly on the Github website. Now clone the repository and in the repo create a new python file.
In the python file simply write "print("Hello World")" and save. Now commit the new file and push
your changes. Go back to the Github website and verify that the python file you pushed is present.

Done


Question 7  GOOD
If your friend made changes to the repo and you want to update your local copy to reflect the
changes what git command(s) can use you in order to do so.

You would first cd into the folder that the file is in, then git pull to recieve any new changes.


"""
Comments:
Nice work. For question 7 you do not have to cd into the folder that the file is in. You only have to
cd into any folder or location within the repo.
'''