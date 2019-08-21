"""
Now that we looked at how to read and write data with text files lets talk about JSON data and files.
JSON is different then just regular text files and has its advantages (as you will see). So lets begin
with what JSON is.
"""

"""
You can think of JSON as data but formatted into a data structure that is basically a dictionary.
Also to work with JSON you will need to import json so lets do that now.
"""

import json

"""
Now lets see an example of a JSON file and see how it compares to regular text files
(Open up sample_json_data.json and compare with sample_data_2.txt from Extra_Data)
So yeah it does look a bit weird, but you can always search up more example online to get use to it.
It really does look like a dictionary right? Well that is basically what it is. There are four keys
each with a value. Ok lets see how we read in a JSON file.
"""

def reading_from_json():
    # Note: if the file does not exist we will get an error
    file = open("sample_json_data.json", "r")
    data = json.load(file)
    print(data)
    print(data["apple"])
    file.close()

#reading_from_json()

"""
Ok so this time around when we read the data it is not a string. The JSON file when read gets understood and
converted into a dictionary. So really you can think of JSON as reading and writing but dedicated for dictionaries.
It is great for storing information about objects such as people. We can use JSON for everything and never touch
text files but sometimes it is better to use text files (it all depends on the situation). Also, with JSON we do not
have to worry about \n which is nice. Ok now lets look at how to write to a JSON file.
"""

def writing_to_json():
    file = open("sample_json_data_2.json", "w")
    my_data = {"cash": 0, "home": "i got null", "poor": True}
    json.dump(my_data, file)  # dump the data into the file to save it
    file.close()

#writing_to_json()

def reading_from_my_saved_data():
    file = open("sample_json_data_2.json", "r")
    my_data = json.load(file)
    print(my_data)
    print(type(my_data["cash"]))  # JSON preserves the type of our data
    file.close()

#reading_from_my_saved_data()

"""
So with JSON you still need to specify the file mode, but usually we just stick with "r" for reading and "w" for writing.
Also, notice how reading from JSON preserves the type of the data so we don't have to convert it ourselves like with
text files. 
"""

"""
Ok that is pretty much all you need to know for JSON. Now lets apply this to the EmailManager case
and see that using JSON makes our life way easier (well at least in this example)
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
            self.emails = json.load(file)

    def save_data(self, file):
        if not self.check_file_exist(file):
            # create the file
            file = open(file, "w")
            file.close()

        # open connection to file containing saved data
        file = open(file, "w")
        json.dump(self.emails, file)

    def check_file_exist(self, file):
        return os.path.exists(file)


def using_email_manager():
    EM = EmailManager()
    # Load the saved data
    EM.load_data("email_data.json")
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
    EM.save_data("email_data.json")

#using_email_manager()
