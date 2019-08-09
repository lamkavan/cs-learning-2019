"""
For this lesson we talk about multidimensional list which is a very important concept
with a wide variety of practical uses. We learn what they are, how to work with them, how
to solve problems with them and finally what they can be used for.
"""

# We begin with simple examples of multi dim list
multi_list = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
print(multi_list)
print(multi_list[1])
print(multi_list[0][2])
print(multi_list[2][2])
print(len(multi_list))


# We can even start off with a 1 dim list and dynamically turn it into a multi dim list
a_list = [1, 2, 3]
a_list.append([1, 55, 88])
print(a_list)


# There is a nice notation we can use to describe multi dim list it is n by m
# n is like a variable that will take on a number once we know its value.
# For example, if we have a 3 by 3 list (often times written as 3 x 3) then the
# list could look like... [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# We could also write the list like this so that it is more readable
# [[1, 2, 3]
#  [4, 5, 6]
#  [7, 8, 9]]


# Alright now let’s solve some problems involving multi dim list
# Question 1
# Write a function that takes in a 3 by 3 list of numbers and prints the list
# row by row but invert the order of the rows
def reverse_multi_list(multi_list):
    for sublist in multi_list:
        sublist.reverse()
        print(sublist)
reverse_multi_list([[11, 12, 14], [34, 45, 56], [78, 90, 0]])


# Question 2
# Write a function that takes in a list of ints. Turn the list into a a multi dim list
# such that the first sub list contains all the even numbers and second sub list contains
# only the odd numbers. Do not return the list just print it to the console
def split_to_even_and_odd(list_of_ints):
    odd_list = []
    even_list = []
    master_list = []

    for i in (list_of_ints):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    master_list.append(odd_list)
    master_list.append(even_list)
    print(master_list)
split_to_even_and_odd([1,3,5,6,7,10,99])


# Question 3
# Write a function that takes a list of information where each sub list contains a
# user id, name, age, height in that order. The function will also take in a user id and name.
# The function will find the sub list corresponding to the user id and change the name to the name
# given as a parameter to the function and return the final list with the correct name change
def update_name(data, user_id, new_name):
    for person in data:
        if person[0] == user_id:
            person[1] = new_name
    return data

print(update_name([[1, "john", 5, 30], [2, "bob", 6, 50]], 1, "ling"))



# What can multidimensional list be used for?
# Multidimensional lists has many applications.
# For example in visual computing and the organization of data with commonalities.
