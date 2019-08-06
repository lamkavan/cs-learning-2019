"""
Below are the solutions to the recursion questions from Homework 4
Also, the solutions does not include the sentences that describe the base and recursive cases
as that is obvious from the code.
"""

# Question 1
# We assume the user enters a valid input. For example you can assume user will not do f(-10)
def f(n):
    # The 3 base cases
    if n == 1:
        return 5
    elif n == 2:
        return 6
    elif n == 3:
        return 7
    # Recursive case
    else:
        return (2 * f(n-1)) + (3 * f(n-2)) - (f(n-3))
print(f(4))


# Question 2
def ask_age():
    age = int(input("What is your age? "))
    if age >= 10:
        ask_age()
    else:
        print("You are a child")
ask_age()


# Question 3
def recursive_linear_search(list_of_num, num):
    # Ensure the list is not empty
    if len(list_of_num) == 0:
        print("List is empty")
        return
    # Base case
    elif len(list_of_num) == 1:
        if list_of_num[0] == num:
            return True
        return False
    # Recursive case
    else:
        return (list_of_num[0] == num) or recursive_linear_search(list_of_num[1:], num)
print(recursive_linear_search([5, 6, 8, 22, 55, 100, 3243, 1, 0], 784))