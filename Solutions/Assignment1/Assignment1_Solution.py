"""
Solutions for Assignment1
Note: The docstrings will not be done in the solutions
"""

# Question 1
"""
a) // is the div operator and it is a division but the floor of the result os returned.
This means that that the numbers after the decimal point are removed.

b) ** is the exponent operator. Nothing special it just does exponents.

c) % is the modulus operator and this returns the remainder from the division.

d) * is the multiplication operator

e) / is the division operator
"""


# Question 2
def question2():
    name = input("Enter you name: ")
    age = input("Enter your age: ")
    print("Hello " + name + " your age is " + age)


# Question 3
"""
If you enter 1/0 in Python you will get a division by zero error. This happens because
Python does not have a built in way to deal with division by zeros which in math we 
consider "impossible". 
"""


# Question 4
"""
There are many different data types in Python. Three examples are ints, strings and list.
Ints are integers. Strings are a collection of characters. Lists are a collection of objects.
"""


# Question 5
"""
There are actually two issues with the code. The first is the tab on the print line. This
will actually cause an error as Python treats tabs and spaces specially. In other words, 
spaces and tabs in Python matter and can not be randomly used. The second problem is the 
x+y on the print line. X is an int but y is a string and you can not add an int to a string.
"""


# Question 6
def question6(num):
    if num > 50:
        print("Wow that is a big number")
    elif num < 50:
        print("That is a small number")
    else:
        print("50 is my lucky number!")


# Question 7
def question7(num1, num2):
    if num1 > num2:
        print(str(num1) + " is bigger than " + str(num2))
    elif num1 < num2:
        print(str(num2) + " is bigger than " + str(num1))
    else:
        print("The two numbers are equal")


# Question 8
def question8(temp_in_F):
    # Note C = (F - 32) * (5/9)
    temp_in_C = (temp_in_F - 32) * (5/9)
    print("The temp in degress Celsius is " + str(temp_in_C))


# Question 9
"""
The difference between the two version is with the if statements. The two version accomplish
the same task, but code snippet 1 is better than snippet 2. The difference is that if x>5 then
the elif part will not run from snippet 1. However, code snippet 2 will always run the second if
statement even if x > 5. This is redundant and a waste of computational power. 
"""


# Question 10 (sample answer)
def something_cool():
    # The cool part here is the \n . It is the newline character. Basically tells Python to move to next line
    print("Hello world\n" * 10)
