"""
In this lesson we discuss dictionaries and what they can be used for.
You can think of a dictionary as a list but instead of indexing the using
an index number, you index using the name you assigned to the spot in the dict.
There are many differences between list and dictionaries we will discuss those first.
"""


# We begin with an easy example
my_dict = {"a": 11, "b": 21, "c": 32}
print(my_dict["a"])
print(type(my_dict["a"]))
print(my_dict)


# Looks easy right? Well there are a couple things we need to cover.
# First, some basic terminology. Each thing in the dictionary is called
# a key-value pair. For example, "a": 1 is a key-value pair. The key is "a"
# and 1 is the value. To get to the 1 you must have/know the key which is "a".
# Second, the keys in a dictionary must be unique so this means no duplicates.
# If there are duplicates then the latest one is used and previous one is removed.
# Third, the order of the key-value pairs in the dictionary is not determinate in
# old versions of python. This means you can never know the ordering of the pairs
# in the list. Anyhow this is not something you need to worry about. To prove it...
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict.keys(), "Ok so far it makes sense.")
my_dict["hello"] = 12
my_dict["bye"] = 1
my_dict["abc"] = 99
print(my_dict)
print(my_dict.keys(), "Still good!!")


# Fourth, the keys have limitations. The keys can only be data types that are immutable.
# This means we can not use a list as a key. The values have no restrictions.
# my_dict[[1, 12]] = "hello" doing this gives an error as expected.


# Alright finally lets solve a problem involving dictionaries
# Write a function that takes in a dictionary and print the key value pairs
# but only every other one starting with the second.
def show_every_other_one(input_dict):
    indicator = -1
    for key in input_dict.keys():
        if indicator == 1:
            print(key, input_dict[key])
        indicator *= -1


# Finally mention what dictionaries can be useful for
# 1) Maybe you have a list student ids and you want to be able to
#    determine the a student's name based on their id really quick
# 2) Can be used for counting occurrences of things
# 3) Simple data encryption.
