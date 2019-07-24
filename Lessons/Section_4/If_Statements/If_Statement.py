"""
If statements allows the program to react differently depending on the situation.
It can depend on many things such as the value of certain variables or a combination
of variables. If statements are very useful and can be used to break up your code
into easy to understand pieces.
"""

# lets begin with simple if statements and also cover a very important concept
# Important concept: Version 2 is usually the better case. The behaviour of the code
# with and without the elif.

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


# There is another thing that many people don't know and it is the fact that Python is lazy
# when it comes to certain if statements. For example...
x = 5
if x == 5 or x/0 == 1:
    print("ggggg")
# This does not crash since there is an OR and Python is lazy. To better explain...
# When you use an OR the predicate is true when at least one of the parts is true
# so when the first part is true there is no need to check the second part as the predicate
# will evaluate to true anyways. However if it was a AND then it would crash since the AND
# logical connector requires that all parts be true to evaluate to true. Thus everything
# must be checked. Watch out, the AND operator can also be lazy... if the first part
# is false then there is no need to check the second part as the whole thing is false
# when at least one part is false. The following example shows this.
x = 5
if x == 99 and x/0 == 1:
    print("ggggg")
else:
    print("No crash!!!")


# Now lets solve a problem involving if statements
# Note: There are much better solutions to this problem, but we want to use if statements
# The problem is that we want to write a function that takes a time in 24hr format and converts it to 12hr format
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


# Testing the function...
convert_to_12hr(13)
convert_to_12hr(1)
convert_to_12hr(0)
convert_to_12hr(15)
convert_to_12hr(24)
convert_to_12hr(12)


