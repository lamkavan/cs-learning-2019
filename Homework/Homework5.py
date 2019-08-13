"""
This homework will give you a chance practice making your own data type/objects.
This is of course what we call classes in Python. This homework is not very hard, good luck


Question 1
Write a class called Computer. A Computer will need to have a name, ram_size, cpu_speed, hdd_size and price.
If you don't know what ram or hdd is then google it and learn. With the Computer class you should be able to
print its name, ram size, cpu, price and hdd_size. Have a separate method to print each attribute. Also, write
another method (__str__) to be able to see all the details just by using print. Finally, include a method that allows
the user to be able to change the price of a Computer.


Question 2
Look back at your class from question 1. I want you to add methods so that we are able to compare Computers together
by price. So I can do stuff like...
x = Computer(Blah, 1000)
y = Computer(Blah, 2000)
print(x == y)    --- Should print False
print(x < y)     --- Should print True


Question 3
Write a function that takes a single Computer object and a list of Computer object as input. The function will return
a new list of all the Computers with a price equal to or less then the single Computer object given as input.


Question 4
Write a class called EmailManager. We will use this class as a database for emails. The class will be able to store
a large collection of email address. When the class is initialized the database should be empty as in there are no
emails stored inside yet. Then there will be a method that allows the user to be able to add an email to the database.
The email will be linked to a name so when adding a new email a name needs to be also given as input. There will be a
method that is able to tell the user the name that is attached to an email. Also, if the user attempts to add an email
that already exist in the database then do not add it and print an appropriate message to inform the user. There should
also be a way to delete emails off the database. Below is an example of its usage...
[IN]  email_database = EmailManager()
[IN]  email_database.add_email("john@gmail.com", "john")
[IN]  email_database.add_email("dingdong@live.ca", "kate")
[IN]  email_database.add_email("dingdong@live.ca", "bob")
[OUT] "This email already exist. Can not add it."
[IN]  email_database.name("dingdong@live.ca")
[OUT] "kate"
[IN]  email_database.remove("dingdong@live.ca")
[OUT] "dingdong@live.ca owned by kate was removed from the database"


Question 5
Go back to the EmailManager class and add a method that returns the number of emails in the database.
The user should be able to get the number of emails simply by using len.


Question 6
Go back and make sure you have answered all questions completely.
"""
