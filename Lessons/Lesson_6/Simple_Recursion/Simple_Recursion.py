"""
In this lesson we will learn about recursion in programming. You may have heard of recursion
elsewhere perhaps from math class. Recursion in programming follows the same principle of recursive
math functions in mathematics. To simply put it, recursion is when we have a function that calls itself
during its execution. You may have seen a function call another function, but when a function calls itself
that is what we call a recursive function.
"""

# For example...
def a_recursive_function(inputs):
    # Blah Blah
    inputs2 = inputs
    a_recursive_function(inputs2)
    # Blah Blah
    pass

"""
A recursive function can take in as many parameters as you like. So far recursion seems pretty straight forward
right? Well... it gets more complicated. There are a couple of concepts and terminology that needs to be covered.
First we will talk about something called a base case and recursive step. To explain this we will take a look at
a classic example in which we compute the factorial of some number.
"""

"""
Side note: A factorial is a unary mathematical operator. It is denoted by ! (yes an exclamation mark). The inputs
are any positive whole numbers including zero. Every other number is not a valid input to factorial. The factorial
of a number n is just the product of all the positive whole numbers that come before it including itself. So 
4! = 4 * 3 * 2 * 1 and 3! = 3 * 2 * 1. A special case is 0 what is 0 factorial? Well you don't need to know why, but 
0! = 1. Also 1! = 1. Now in general n! = n * (n-1)! can you see why? If not ask your teacher and do not proceed until
you understand why. Alright now we can go back to programming.
"""


"""
So below is a recursive function that computes the factorial of a given number n.
It is not super complicated but you need to understand what we mean by base case
and recursive step. The way you need to think about recursion when solving a problem
is how you can break the problem down and be able to answer the question using the previous
answer. The base case is the case where you can not break down the current problem any further
the current problem has an answer that is very trivial/easy. The recursive cases are the cases
that can be dealt with by breaking down the problem into smaller pieces. The recursive step is
also the case where you would call the same function. We call the same function to solve the
smaller pieces. Your teacher will draw diagrams to help you better understand. 
"""
# Note: This function assumes the user will not enter a number that has no factorial.
# If we wanted to user proof this we can just add an if statement at the very start
# that check if n is >= 0 otherwise we quit and do nothing.
def factorial(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive step
    return n * factorial(n-1)

# Lets try out our factorial function
print("4! =", factorial(4))
print("4! =", factorial(0))
print("4! =", factorial(5))

"""
How can you solve the same problem of computing a factorial without using recursion?
Well you could just use a for loop, but that will look a bit more complicated. This is
one of the nice things about recursion. It can make your life a lot easier and even make
your code shorter and easier to read/understand. Generally speaking recursion is a powerful
tool and is used in many different applications. However, recursion may not always be the 
best solution and also has its downfalls. We talk about these later, but first lets do
two other examples of recursion.
"""

# Question 1
# Write a recursive function to return the nth number in the Fibonacci sequence.
# Again we assume the user does not enter an invalid input. n must be 1 or greater
# Note: F_n = F_n-1 + F_n-2
def fib(n):
    # Base cases
    if n == 1:
        return 0
    elif n == 2:
        return 1
    # Recursive cases
    return fib(n - 1) + fib(n - 2)
print("The 5th fib number is", fib(5))
print("The 1th fib number is", fib(1))
print("The 7th fib number is", fib(7))


# Question 2
# Write a recursive function that takes in a multidimensional list of numbers and prints to the console
# all of the numbers each on different lines
def elements_of_nested_list(input_list):
    for element in input_list:
        # Recursive case
        if type(element) == type([]):
            elements_of_nested_list(element)
        # Base case
        else:
            print(element)
elements_of_nested_list([1,2,3,[99,100], [], [33, [], [66,7,[999999]]]])


"""
Can you imagine trying to answer question 2 without using recursion (great interview question)? It is a lot easier
with recursion. Anyhow, hopefully the examples gives you a better understanding of recursion. Now lets move away from
programming and go towards the Computer Science side of recursion. The first thing we need to understand is what
is going on behind the scenes when we call functions? I will try to explain this as simple as possible.
There is something called the stack. You can think of the stack as dedicated memory for storing information
about the program that is running. Variables, values and functions are stored here. In the stack there are things called
stack frames. You can think of the stack as the cabinet space and a stack frame as a plate. Everytime you make a function
call a new stack frame is added to the top of the stack and when the function stops and returns the stack frame for it
gets removed. Your teacher will draw a diagram to help you understand. So... the amount of space on the stack is limited
and if you keep on adding stack frames to it the stack may overflow. This is what we call a stackoverflow. Lets see an 
example. 
"""

# Stackoverflow example
def overflow():
    overflow()
overflow()


"""
Crazy right? This highlights one of the disadvantages of using recursion. If your problem requires too many recursive
calls then you may get a stackoverflow and may not be able to solve the problem due to hardware limitations. Other
downsides includes harder debugging, hard to understand for beginners and easy to make mistakes. This issue with
stackoverflow really emphasises the need for a base case. In the base case you should not be calling the function so
that stops the computer from adding more to the stack. Without a base case you will keep on making recursive calls until
you hit a stackoverflow or max recursive depth error. This is why sometimes using for loops may be a better solution
than using recursion. Using for loops does not require you to make additional function calls thus you are not adding more
frames to the stack so you can not get a stackoverflow error. Makes sense? If not... welcome to computer science.
"""
