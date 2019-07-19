### The following describes basic docstrings for Python ###

# We use docstrings to document our code. Documenting the code makes it easier to read
# and understand. It is good practice, but not required for the code to work.

# We only cover docstrings for classes and functions/methods here.

# Note that there are many formats for docstrings and depending on which one you
# use the documentation will look a bit different.

# We begin with two examples of writing docstrings for functions.
def print_list_contents(input_list):
    """
    Prints to the console the elements of input_list with each element
    on a new line

    Args:
        input_list (list): A list of elements

    Returns:
        None
    """
    for item in input_list:
        print(item)


def compute_multiplication(input_list, factor):
    """
    Takes a list of numbers, input_list, and returns a list where each number
    is replaced with the product when multiplied with factor

    Args:
        input_list (list of num): A list of numbers
        factor (int, float): A number to multiply list number(s) with

    Returns:
        list: The original list with all the numbers multiplied by factor
    """
    return [num * factor for num in input_list]


# Ok do you understand the examples? Not too bad right? Anyhow below is the general format.
def function_name(arg1, arg2, arg3):
    """
    <Description of function goes here>

    Args:
        arg1 (<type of arg1>): <Description of arg1>
        arg2 (<type of arg2>): <Description of arg2>
        arg3 (<type of arg3>): <Description of arg3>

    Returns:
        <return type>: Description of the return
    """
    # Blah blah blah (this is where the actual function is and is not part of docstring)
    pass


# Ok now lets talk about classes and the methods under a class. The best way to learn is just to see an example.
class Car:
    """
    A car (Here we want to describe the class)

    Attributes:
        age (int): The car's age
        color (str): The car's color
        name (str): The car's name in all upper case letters
    """

    def __init__(self, age, color, name):
        """
        The constructor for car

        Args:
            age (int): The car's age
            color (str): The car's color
            name (str): The car's name
        """
        self.age = age
        self.color = color
        self.name = name.upper()

    def car_name(self):
        """
        Prints the car's name to the console

        Returns:
            None
        """
        print(self.name)


# Alright notice how the constructor method does not have the return part in the docstring.
# This is because the constructor should not return anything other than none.
# Also notice that we never include self in the Args section of the docstring.
# The docstrings for methods is the same for functions