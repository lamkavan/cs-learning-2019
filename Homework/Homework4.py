"""
The questions below will ive you a chance to practice writing recursive algorithms.
The questions are not very difficult and there is not a lot of code to write, but you
will need to think carefully as it may be hard to think recursively as a beginner
computer scientist. Remember that doing these type of questions is easier once you think
about how to solve the problem by using the solution to the simpler versions of the problem.

Note: For each question you will have to write code, but I also want you to state in words what the
base and recursive cases are.

Question 1
Write a recursive function that models the following equation... f(n) = 2f(n-1) + 3f(n-2) - f(n-3) for n >= 1
The recursive function will take a single int as input and return the output of the equation.
The input is n and n >= 1. So if n = 5 we want the 5th number in the sequence. In addition you are
given that f(1) = 5, f(2) = 6 and f(3) = 7. Hint: there are three base cases and one recursive case.
Start the function like this ...
def question1(n):
    blah
    blah


Question 2
Write a recursive function that takes no inputs. This function will ask the user an
age (using input("What is your age")). If the age >= 10 then ask again. Keep asking until the age is < 10
at which point print to the console "You are a child" and stop asking. The non-recursive version is as follows
def ask_age():
    age = 9999999
    while (age >= 10):
        age = int(input("What is your age"))
    print("You are a child")


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


Question 4
Go back and check the solutions. Test your code. Does it work? If it does not work try to fix it.
"""