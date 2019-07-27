"""
Have you ever wondered how we can get input from the user running the code?
Well it os actually pretty easy. The following lesson will show you.
"""

# Its is so easy we can just do an example
name = input("What is your name? ")
print("Hello", name)


# One thing you need to know is that input always returns a string
# So if you were to asking the user for their age using input then
# do not forget to convert that to an int if you want to use the age
# as a number instead of a string. For example...
age = int(input("What is your age? "))
print("Next year you will be", age + 1, "years old.")
# Note the age + 1 will not work unless you convert the age into an int


# If the user just presses return or enter then the empty string is returned ie/ ""
# This is good to know once we start validating the user input.
