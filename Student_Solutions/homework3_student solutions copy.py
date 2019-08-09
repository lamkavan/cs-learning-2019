# Shruti Kasera
# 07.08.19
# Homework 3

'''
 Question 1
 Write a function that takes a n by 2 list of numbers and turns it into n by 1 list of numbers.
 Basically convert it into a regular list and return the new list. Do not use any list methods.
For example, [[1, 2], [99, 100], [12, 11]] becomes [1, 2, 99, 100, 12, 11]
 '''


def multi(single_list):
    empty_list = []
    for i in single_list:
        for j in i:
            empty_list.append(j)
    return empty_list


print(multi([[1, 3], [4, 7], [9, 5]]))

"""
Comments
Nice... but the variable names are poor. empty_list --> flatten_list  and single_list ---> multi_list
Note: This question would be a lot harder if it were a n by n list. Here recursion would be nice.
"""

'''
Question 2
Write a function that takes a 3 by n list of numbers. Each group (there are three) is a list of n numbers.
So Each group has the same number of numbers. The function will print to the console letting the user know
if there are any duplicate numbers between each distinct pair of groups. There are 3 distinct pair of groups.
'''


def distinct(diff_list):
    list_1 = diff_list[0]
    list_2 = diff_list[1]
    for l in list_1:
        if l in list_2:
            print("There are the same numbers in sublist 1 and 2")

    list_1 = diff_list[0]
    list_2 = diff_list[2]
    for s in list_1:
        if s in list_2:
            print("There are the same numbers in list 1 and 3")

    list_1 = diff_list[1]
    list_2 = diff_list[2]
    for k in list_1:
        if k in list_2:
            print("There are the same numbers in list 2 and 3")


print(distinct([[1, 2, 3], [4, 5, 3], [7, 8, 9]]))

"""
Comments
Nice, but your print messages are not correct. The sublist do not have the same numbers otherwise they are the same.
You should say that there are duplicates. 
"""

'''
Question 3
Write a function that takes exactly 20 numbers and returns a 5 by 4 list which contains all the 20 numbers.
'''


def one_list(nums_20):
    big_list = []
    for f in range(0, len(nums_20), 4):
        big_list.append(nums_20[f:f + 4])
    return big_list


print(one_list([f for f in range(20)]))

"""
Comments
Good
"""

'''
Question 4
Write a function that takes no input. The function will use input to get data from the user. Specifically,
the function will ask the user for a day, name and an age separated by a commas (no spaces).
The function will ask for this input 10 times. You can assume that the day will either be Monday or Friday.
There are no restrictions for the name and age. The input will store all this data in a multidimensional list
and at the end return the list. The list will have the following structure, there will be two main sub list in
the outer most list. The first sub list is for all the people on Monday and the second sub list is for all the people
on Friday. For each of those sublist there are two sublist. One for people 18 and older and one for people less than 18.
For example, if the user enter monday,john,20 then the list should look like [[["monday,john,20"], []], [[], []]]
'''
''


def info():
    end_list = [[[], []], [[], []]]

    for i in range(10):
        user_input = input("Enter name, day, age: ")
        new_userinput = user_input.split(",")
        if user_input[0].lower() == "monday":
            if int(user_input[2]) >= 18:
                end_list[0][0].append(user_input)
            else:
                end_list[0][1].append(user_input)
        elif user_input[0].lower() == "friday":
            if int(user_input[2]) >= 18:
                end_list[1][0].append(user_input)
            else:
                end_list[1][1].append(user_input)

    return end_list

"""
Comments
Good
"""


'''
Question 5
Write a function that takes a list of list of numbers so n by m. The function will return true if the list is square and false otherwise.
A list is square if n==m. So the number of sublist lists is equal to the number of numbers in each sublist. If, you
to draw out the list properly it would be in the shape of a square. In math (liner algebra) we can this a square matrix.
So an example of a square list would be [[1, 1, 1], [2, 2, 2], [3, 3, 9]]
'''


def square(is_square):
    equal_list = len(is_square)
    for m in is_square:
        if len(m) != equal_list:
            return False
        else:
            return True


print(square([[1, 2], [2, 4]]))

"""
Comments
The function name is bad you should call it is_sqaure. The input to the function is bad it should be called input_list or something similar.
Your function is incorrect but close to the correct answer. Your function will only check to see if the the first row has the same amount of numbers
as rows. Your function will not work for list like [[1,2,3], [1,2] , [1]]
"""

'''
Question 6
Write a function to draw a equilateral triangle given a height parameter. For example if height = 5 draw the following
     *
    ***
   *****
  *******
 *********
'''


def triangle(height):
    bottom = ((height - 1) * 2) + 1
    stars = 1

    for q in range(height):
        spaces = bottom - stars
        print(" " * (spaces // 2) + ("*" * stars) + " " * (spaces // 2))
        stars += 2


print(triangle(13))

"""
Comments
Very good. However, I am not sure why you use print around triangle(13) as that would print none as the function does not return anything.
"""


'''
Question 7
Write a function to draw a letter P given a height parameter that is at least 4. For example if height = 4 then draw the following
 *****
 *   *
 *****
 *
Ugly right? If the height parameter is 7 then print the following
 *****
 *   *
 *****
 *
 *
 *
 *
'''


# ask question
def p(length):
    if length < 4:
        return
    else:
        print("*" * 5)
        print("*" + (" " * 3) + "*")
        print("*" * 5)
        print("*\n" * (length - 3))


print(p(8))

"""
Comments
Nice work!
"""
