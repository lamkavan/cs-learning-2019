"""
Solutions for Assignment2
"""

# Question 1
def function1(input_str):
    for i in range(25):
        print(input_str)


# Question 2
"""
An infinite loop is a loop that keeps on looping and never stops. It is usually observed in while loops
especially when the condition on the while loop is trivially always True. Infinite loops are also possible
with for loops as well. For example...

nums = [1,2,3]
for num in nums:
    print(num)
    nums.append(num + 1)
    
Because we keep adding more to the list the loop will never stop.
"""


# Question 3
"""
Python list is a data structure that allows you to store a collection of objects. You can store
what ever you like in them even other list. They can be useful for grouping a collection of related data.
"""


# Question 4
"""
Dictionaries are like list but instead of indexing with indices we index with the keys. It is like replacing the
indices with what we want. The keys can only be of types that are immutable. The values can be anything they want.
They can be useful in situations where you want to be able to retrieve data based on some given label that you assign.
"""


# Question 5
"""
Basically a method is like a function, but it is under a class or belongs to a object. Some examples of 
methods for dictionaries include .keys() .clear() and .values()
"""


# Question 6
def question6(list_of_num):
    output_nums = []
    for num in list_of_num:
        if num < 50 or num > 85:
            output_nums.append(num)
    return output_nums


# Question 7 (Hard question without recursion)
def question7(input_list):
    # We need to flatten the list first
    flatten_list = str(input_list)
    flatten_list = flatten_list.replace("[", "")
    flatten_list = flatten_list.replace("]", "")
    flatten_list = flatten_list.split(",")
    flatten_list = [int(num) for num in flatten_list if num != "" and num != " "]

    # Now check for duplicates
    for num in flatten_list:
        temp = flatten_list.copy()
        temp.remove(num)
        if num in temp:
            return False

    # If we get here then there are no duplicates
    return True


# Question 8
def count_chr(string):
    chr_dict = {}
    for chr in string:
        if chr in chr_dict:
            chr_dict[chr] += 1
        else:
            chr_dict[chr] = 1

    for key in chr_dict.keys():
        print(key, ":", chr_dict[key])


# Question 9
def print_stars():
    for i in range(9, 0, -1):
        print("*" * i)


# Question 10
# This is a challenge question and solutions will not be provided
# Speak with teacher for help