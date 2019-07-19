"""
Solutions for Homework1
Note: The docstrings will not be done in the solutions
"""

# Question 1 solution 1
def get_num_of_digits(num):
    num_as_str = (str(abs(num))).replace(".", "")  # we must use the positive version)
    return len(num_as_str)


# Question 2
def print_triple_str(text):
    for chr in text:
        print(chr + ((" " + chr) * 2))


# Question 3
def convert_to_list_of_str(list_of_int):
    list_of_str = []
    for num in list_of_int:
        list_of_str.append(str(num))
    return list_of_str


# Question 4
"""
No it is not always possible to to convert a string into an int. If the string does not
have a natural int representation then it will not work. For example, int("Hello") will not
work. However it is always possible to convert an int to a str. In fact you can always convert a string
into a list as a string is just a collection of characters and each character can be stored in one cell
within a list.
"""


# Question 5
"""
Aliasing is when two or more variables reference to the same object stored in memory. Just like two separate keys
to the same house. An example would be doing a = [1,2,3] and then doing b = a. Aliasing however does not occur with
ints. The reason is because aliasing only occurs with mutable objects such as list. An int is immutable so aliasing
will not occur. If you did a = 2 and b = a what happens is that another int object with value 2 is made and assigned
to b instead of b being assigned to the same int object as a. 
"""


# Question 6
"""
range basically builds a list like object containing the numbers in a specified range. Note it is not an actual list object.
range(1,10) gives the numbers from 1 to 9. The first number is the starting point and the second number is the upper limit.
Note that the upper limit will never be reach. The list stops at 9. In general, range will also minus one from the 
upper limit. range(1,10,2) is basically the same thing but the third parameter tells range to jump by 2 instead 
of going up by 1s which is the default. So 1, 3, 5 ...
"""