"""
Solutions for Homework2
Note: The docstrings will not be done in the solutions
Note2: There are many ways to program something
"""

# Question 1
def interchange_strings(str1, str2):
    interchanged_string = ""
    # We make copies here since it is good practice not to mess with the inputs
    # You only have to make copies if you plan on changing the input strings
    str1_copy = str1
    str2_copy = str2

    while str1_copy != "" or str2_copy != "":
        if str1_copy != "":
            interchanged_string = interchanged_string + str1_copy[0]
            str1_copy = str1_copy[1:]
        if str2_copy != "":
            interchanged_string = interchanged_string + str2_copy[0]
            str2_copy = str2_copy[1:]

    return interchanged_string


# Question 2
def is_palindrome(str1):
    if str1 == "":
        return False
    str1_reversed = str1[::-1]
    if str1 == str1_reversed:
        return True
    return False


# Question 3
def count_vowels_and_consonants(str1):
    vowels = ["a", "e", "i", "o", "u"]
    num_of_vowels = 0

    for character in str1:
        if character in vowels:
            num_of_vowels += 1

    print("The word " + str1 + " has " + str(num_of_vowels) + " vowels.")
    print("The word " + str1 + " has " + str(len(str1) - num_of_vowels) + " consonants.")


# Question 4
def cap_ever_other_letter(str1):
    str1_cap = ""
    key = 1  # use this to determine if we should cap letter or not

    for character in str1:
        if key > 0:
            str1_cap += character.upper()
            key *= -1
        else:
            str1_cap += character
            key *= -1

    return str1_cap


# Question 5
def find_and_replace(str1, str2, str3):
    return_string = ""
    while str1.find(str2) >= 0:
        return_string += str1[:str1.find(str2)] + str3
        str1 = str1[str1.find(str2) + len(str2):]
    return_string += str1
    return return_string


# Question 6
def remove_white_space(str1):
    new_str = ""

    for character in str1:
        if character != " ":
            new_str += character

    print(new_str)


# Question 7
def print_star_triangle(height):
    for level in range(height):
        print("*" * (level + 1))


# Question 8
def print_chr_occurrence(str1):
    dic_of_chr = {}

    for character in str1:
        if character in dic_of_chr:
            dic_of_chr[character] += 1
        else:
            dic_of_chr[character] = 1

    for key in dic_of_chr.keys():
        if dic_of_chr[key] > 1:
            print(key + " --- This character appeared " + str(dic_of_chr[key]) + " times")


# Question 9
"""
Tuples use round brackets while a list uses square brackets. Also, lists are mutable while tuples are not.
"""


# Question 10
"""
Methods for tuples include count() and index(). In fact these are the only two official methods for tuples in Python.
We notice that Tuples do not really have any methods and the methods that do exist do not actually modify the tuple. 
"""


# Question 11
"""
Tuples can be useful in many situations and is generally used for storing static data.
One example is when you want a collection of information or constants that you do not want to change. 
Using a tuple in this case makes it easier to manage the static information and ensure that you do 
not modify the static information by accident.
"""


# Question 12
"""
No, aliasing does NOT occur with tuples since tuples is a immutable data type. Remember that aliasing can only occur
with mutable data types such as list.
"""