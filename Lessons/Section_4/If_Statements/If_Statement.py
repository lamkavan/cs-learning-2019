"""
You should already know what if statements are and how to use them, but there is something
that a lot of people misunderstand
"""
# Version 1

x = 6
if x > 5:
    print("hello")
if x < 5:
    print("world")

# OR

# Version 2

x = 6
if x > 5:
    print("hello")
elif x < 5:
    print("world")

"""
Version two is better
"""

# There is another thing that many people don't know. So take a look
x = 5
# Just note this. it will crash.
#if x/0 > 1:
#    print("hhh")

if x == 5 or x/0 == 1:
    print("ggggg")

# This does not crash since there is an OR and Python is lazy. However if it was a AND then it would crash.


# Now lets solve a problem involving if statements

# The problem is that we want to write a function that takes a time in 24hr formate and converts it to 12hr formate
def convert_to_12hr(time_24hr):
    if time_24hr == 0:
        print("12am")
    elif 11 >= time_24hr >= 1:
        print(time_24hr, "am")
    elif time_24hr == 12:
        print(time_24hr, "pm")
    elif time_24hr == 24:
        print(time_24hr - 12, "am")
    else:
        print(time_24hr - 12, "pm")


convert_to_12hr(13)
convert_to_12hr(1)
convert_to_12hr(0)
convert_to_12hr(15)
convert_to_12hr(24)
convert_to_12hr(12)

