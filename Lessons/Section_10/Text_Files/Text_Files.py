"""
We have a bunch of coding at this point, but one thing we have not done yet is have the ability
to store and retrieve data from outside sources. For example, lets go back to the EmailManager
from homework 5. If we terminated the program we would lose all the emails in the database. The idea
for this lesson is to be able not lose the emails once the program terminates. There are many ways
we can do this but for this lesson we focus on text files.

Ok but before we go straight into the EmailManager we need to learn the basics of reading and writing to a
text file. We begin with reading from a text file.
"""


def reading_from_a_txt_file():
    # We use open get the connection to the file
    # the second parameter is the connection type "r" = read-only
    file = open("sample_data_1.txt", "r")

    # read() looks at the whole file at once
    data = file.read()
    print(data)
    print("-------------------------------------------")

    # Reset the connection
    # we need to do this because we already reached the end of the file so to start from beginning we
    # can restart the connection
    file.close()
    file = open("sample_data_1.txt", "r")

    # readline() looks at the file line by line
    data = file.readline()
    print(data)
    data = file.readline()
    print(data)
    print("-------------------------------------------")

    file.close()
    file = open("sample_data_1.txt", "r")

    # readlines() looks the file line by line and puts each line in a cell within a list
    data = file.readlines()
    print(data)
    print(len(data[0]))  # this prints 16 so \n is considered as one chr NOT two
    print("-------------------------------------------")

    file.close()
    file = open("sample_data_1.txt", "r")

    # We can even iterate over it like a list
    for line in file:
        print(line)
    print("-------------------------------------------")

    file.close()
    file = open("sample_data_1.txt", "r")

    # Ok the first time included too many spaces so lets remove the \n from each line
    for line in file:
        print(line[:-1])

    print("-------------------------------------------")

    # Lets try reading another file but this time it is in a different directory
    file.close()
    file = open("../Extra_Data/sample_data_2.txt", "r")
    for line in file:
        print(line[:-1])

    # Make sure you always close the connection when you are finished
    file.close()

#reading_from_a_txt_file()


"""
Ok pretty easy right? One thing to note is that when you are reading from the file
Python has an internal bookmark that keeps track of how much you read. So when ever we
wanted to start reading from the beginning again we restarted the connection (it is one way to do it).
Also notice how when we read each line it includes a \n. The reason it obvious. The text file uses it to
understand when to start a new line and so does Python. Also note that when reading from a text file
everything is considered a string so if you wanted the age to be considered as an int you will need to
convert it yourself.
"""

"""
Now before we go ahead and try writing to files lets talk about file modes. As you saw, you use open to make a
connection to the file, but we also need to specify the file mode. We have seen "r" which is read-only so
you will not be able to write or modify the file. There are many more file modes that you can use and we won't
cover all of them, but you can easily just search them up.
"""

def writing_to_a_text_file_part1():
    # "w" = write-only
    file = open("sample_data_3.txt", "w")
    file.write("Hello World")
    file.write("I am the best")

#writing_to_a_text_file_part1()

"""
So notice that Python created the file for you it is does not exist. That is nice. Also notice that Python did
not move to a new line after the first print. Python will never move to a new line when writing. You will
have to move it to the next line yourself by using \n (the new line character). So lets try this again.
"""

def writing_to_a_text_file_part2():
    # "w" = write-only
    file = open("sample_data_3.txt", "w")
    file.write("Hello World\n")
    file.write("I am the best\n")

#writing_to_a_text_file_part2()

"""
Alright much better. Wait what!? Did you notice that? Python removed the contents of the file and then started writing
to the file that is the reason why we do not see the previous failed attempt at writing hello world to the file.
So remember when you open a file in "w" mode and you start writing it will move all the old content. Ok what if
you wanted to write to a file without deleting the old stuff? Well its just a matter of using the correct file mode.
"""

def writing_to_a_text_file_part3():
    # "a+" = append to a file with ability to read
    file = open("sample_data_3.txt", "a+")
    file.write("Hellosss World\n")
    file.write("I am the best\n")

#writing_to_a_text_file_part3()


"""
In the above example I used "a+" which allows me to do everything (read and write) without erasing data.
On thing to watch out is that for reading with "a+" the bookmark is initially set to the end of the file
so you will only be able to read the new stuff that you write unless you use seek() which you can learn on
your own time. To read the whole file you can just re-open the file in "r" mode. 
"""

"""
Alright that is pretty much it for the basics. Now lets do something interesting with EmailManager, but using
a simple version of the email manager
"""
import os


class EmailManager:
    def __init__(self):
        self.emails = {}

    def add_email(self, email, name):
        if email in self.emails.keys():
            print("Can not add email as it already exist")
        else:
            self.emails[email] = name

    def show_name(self, email):
        if email in self.emails.keys():
            print(self.emails[email])
        else:
            print("Email is not in database")

    def load_data(self, file):
        if not self.check_file_exist(file):
            # create the file
            file = open(file, "w")
            file.close()
        else:
            # open connection to file containing saved data
            file = open(file, "r")
            for line in file:
                temp = line.split(",")
                email = temp[0]
                name = temp[1][:-1]
                self.add_email(email, name)

    def save_data(self, file):
        if not self.check_file_exist(file):
            # create the file
            file = open(file, "w")
            file.close()

        # open connection to file containing saved data
        file = open(file, "w")
        for email in self.emails.keys():
            file.write(email + "," + self.emails[email] + "\n")

    def check_file_exist(self, file):
        return os.path.exists(file)


def using_email_manager():
    EM = EmailManager()
    # Load the saved data
    EM.load_data("email_data.txt")
    loop = True
    while loop:
        user_input = input("Enter an email and name (separated by comma) or just an email or 1 to quit: ")
        if user_input == "1":
            loop = False
        elif "," in user_input:
            temp = user_input.split(",")
            email = temp[0]
            name = temp[1]
            EM.add_email(email, name)
        else:
            EM.show_name(user_input)

    # Save the data before we exit the program
    EM.save_data("email_data.txt")


#using_email_manager()


