# Shruti Kasera
# 13.08.19
# Homework 4

'''
Question 1
Write a recursive function that models the following equation... f(n) = 2f(n-1) + 3f(n-2) - f(n-3) for n >= 1
The recursive function will take a single int as input and return the output of the equation.
The input is n and n >= 1. So if n = 5 we want the 5th number in the sequence. In addition you are
given that f(1) = 5, f(2) = 6 and f(3) = 7. Hint: there are three base cases and one recursive case.
Start the function like this ...
def question1(n):
    blah
    blah
'''

"""
Comments:
Good job
"""

def question1(n):
    # Base Case
    if n == 1:
        return 5
    if n == 2:
        return 6
    if n == 3:
        return 7
    # Recursive Case
    else:
        return 2 * question1(n - 1) + 3 * question1(n - 2) - question1(n - 3)


print(question1(14))

'''
Question 2
Write a recursive function that takes no inputs. This function will ask the user an
age (using input("What is your age")). If the age >= 10 then ask again. Keep asking until the age is < 10
at which point print to the console "You are a child" and stop asking. The non-recursive version is as follows
def ask_age():
    age = 9999999
    while (age >= 10):
        age = int(input("What is your age"))
    print("You are a child")
'''

"""
Comments:
Good job
"""

def ask_age():
    age = int(input("Enter your age: "))

    # Base case
    if age >= 10:
        ask_age()

    # Recursive case
    else:
        print("You are a child")


ask_age()

'''
Question 3
Here you will implement linear search with a recursive algorithm. If you don't know what linear search is
then don't worry. Basically, the recursive function that you want to write will take a 1 by n list of numbers
and a number as inputs. The function will return true if the number is in the provided list and false otherwise.
The way to do this without recursion is simple and is as follows...
def search(list_of_nums, num):
    for number in list_of_num:
        if number == num:
            return True
    return False
The code above is what we call linear search. Your job is to implement this using recursion.
'''

"""
Comments:
Good job
"""

def search(list_of_nums, num):
    # Base case
    if len(list_of_nums) == 0:
        print("Empty List")
    elif len(list_of_nums) == 1:
        return list_of_nums[0] == num
    # Recursive case
    return list_of_nums[0] == num or search(list_of_nums[1:], num)
