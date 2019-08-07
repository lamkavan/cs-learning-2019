"""
Last time we talked about the basics of recursion. For this lesson we will just do more examples.
So there is no new content to learn here.
"""

# Question 1
# Write a recursive function to output a list of all the three digit numbers you can make with the numbers
# 1, 2 and 3. Repeat numbers are allowed.
def get_all_numbers(numbers, num_of_digits):
    # Base case
    if num_of_digits == 1:
        return numbers
    # Recursive case
    all_suffix = get_all_numbers(numbers, num_of_digits - 1)
    all_numbers = []
    for num in numbers:
        for suffix in all_suffix:
            all_numbers.append(int(str(num) + str(suffix)))
    return all_numbers
print(get_all_numbers([1, 2, 3], 3))


# Question 2
# Write a recursive function to output a list of all the four digit numbers you can make with the numbers 1, 2, 3 and 4.
# Repeat numbers are NOT allowed so 112 and 111 is not allowed.
def get_all_numbers_2(numbers):
    # Base case
    if len(numbers) == 1:
        return numbers
    # Recursive step
    all_numbers = []
    for num in numbers:
        temp = numbers.copy()
        temp.remove(num)
        suffix = get_all_numbers_2(temp)
        for num2 in suffix:
            all_numbers.append(int(str(num) + str(num2)))
    return all_numbers
print(get_all_numbers_2([1, 2, 3, 4]))



# Question 3
# Write a recursive function that returns the largest number from a given multidimensional list of numbers
def largest_num(input_list):
    largest = "Nothing"
    for element in input_list:
        # Special case
        if element == []:
            continue
        # Base Case
        if type(element) != type([]):
            if largest == "Nothing" or largest < element:
                largest = element
            continue
        # Recursive case
        largest_from_sublist = largest_num(element)
        if largest == "Nothing" or largest < largest_from_sublist:
            largest = largest_from_sublist
    return largest
print(largest_num([1, 4, [5, 6, [100, 99]], 66, [], [43, 1000]]))


# Question 4
# Write a recursive function that takes a single dimension list and returns the reverse of that list.
# Note: this can be easily done in one line normally but we are practicing recursion


# Question 5
# Write a recursive function that finds the sum of all the digits of a given whole number. Return the sum.

