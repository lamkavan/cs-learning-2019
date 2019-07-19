"""
As you already know there are many different types in Python
these include but are not limited to int, floats, strings and boolean

The end goal of this lecture is to be able to understand the basic types in
Python and how to convert between types. The first thing we should do is talk
about how to determine the type of something.
"""

# --- Determining the type of something --- #
"""
In Python you can determine the type of an object simply by using the built-in method
called type. Lets try it.

Side note: How do you know if it is a method or a function?
"""

# Ex 1
var = "Hello world"
print(type(var))

# Ex 2
var = "12"
print(type(var))

# Ex 3
var = 12
print(type(var))

# Ex 4
var = 12.2
print(type(var))

# Ex 5
var = [12.2, "bye"]
print(type(var))

# Ex 6
var = {"a" : 1, "b" : 2}
print(type(var))


# --- Changing types --- #
"""
Pretty boring right? However, you can actually do really cool things
if you know the type of an object and are able to convert between different types.
Let me demo
"""

# Ex 1
var = "Computer Bob"
var2 = list(var)
print(var2)


# Ex 2
var = "2"
# print(var + 1) do not do this you can not add a string to an int
print(int(2) + 1)  # this works since we converted the str into an int


# Ex 3
var = "hello"
# print(int(var))  # this does not work since a word can't be converted to a number

"""
So it is pretty easy to change the type and if you ever forget or don't know 
how to convert between two types a simple google search should do the trick.
Finally lets see some more complicated examples where type conversion is used.
"""

# Assume input are valid (for example no negative n values)
def extract_nth_digit(num, n):
    num_str_version = (str(num)).replace(".", "")
    return num_str_version[n - 1]

print(extract_nth_digit(14.567, 1))


def add_ones(num, num_of_ones):
    num_str_version = (str(num)) + ("1" * num_of_ones)
    return num_str_version

print(add_ones(23, 3))
