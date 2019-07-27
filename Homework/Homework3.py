"""
The following questions are to help you get more practice with multidimensional list.
Remember to not comment you code and to also but the title, name and date at the top in comments.
Also, make sure you check the solutions after you finish each question. Furthermore, if you are stuck
on a question check the solution for a hint. For all questions docstrings can be omitted.
"""

# Question 1
# Write a function that takes a n by 2 list of numbers and turns it into n by 1 list of numbers.
# Basically convert it into a regular list and return the new list. Do not use any list methods.
# For example, [[1, 2], [99, 100], [12, 11]] becomes [1, 2, 99, 100, 12, 11]


# Question 2
# Write a function that takes a 3 by n list of numbers. Each group (there are three) is a list of n numbers.
# So Each group has the same number of numbers. The function will print to the console letting the user know
# if there are any duplicate numbers between each distinct pair of groups. There are 3 distinct pair of groups.


# Question 3
# Write a function that takes exactly 20 numbers and returns a 5 by 4 list which contains all the 20 numbers.


# Question 4
# Write a function that takes no input. The function will use input to get data from the user. Specifically,
# the function will ask the user for a day, name and an age separated by a commas (no spaces).
# The function will ask for this input 10 times. You can assume that the day will either be Monday or Friday.
# There are no restrictions for the name and age. The input will store all this data in a multidimensional list
# and at the end return the list. The list will have the following structure, there will be two main sub list in
# the outer most list. The first sub list is for all the people on Monday and the second sub list is for all the people
# on Friday. For each of those sublist there are two sublist. One for people 18 and older and one for people less than 18.
# For example, if the user enter monday,john,20 then the list should look like [[["monday,john,20"], []], [[], []]]


# Question 5
# Write a function that takes a list of list of numbers so n by m. The function will return true if the list is square and false otherwise.
# A list is square if n==m. So the number of sublist lists is equal to the number of numbers in each sublist. If, you
# to draw out the list properly it would be in the shape of a square. In math (liner algebra) we can this a square matrix.
# So an example of a square list would be [[1, 1, 1], [2, 2, 2], [3, 3, 9]]


# Question 6
# Write a function to draw a equilateral triangle given a height parameter. For example if height = 5 draw the following
#     *
#    ***
#   *****
#  *******
# *********


# Question 7
# Write a function to draw a letter P given a height parameter that is at least 4. For example if height = 4 then draw the following
# *****
# *   *
# *****
# *
# Ugly right? If the height parameter is 7 then print the following
# *****
# *   *
# *****
# *
# *
# *
# *


