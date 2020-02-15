"""
The following are the answers to all question from assignment 3 other than the bonus
"""

# Question 1
class Car:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def increase_age(self):
        self.age = str(int(self.age) + 1)


# Question 2
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)

    def get_diameter(self):
        return self.radius * 2

    def get_circumference(self):
        return self.radius * 2 * 3.14


# Question 3
def find_in_text_file(text_file, string):
    line_number = 0
    for line in text_file:
        line_number += 1
        if string in line:
            print(string + "found on line " + str(line_number))
            print(line)
            return
    print(string + "was not found in the text file")


# Question 4
# Note this version sorts from smallest to largest
# Insertion sort will have the easiest time sorting when the list is already sorted
# as this means the while loop condition will  never be true and so the while loop
# will never need to be used
# The case that will be hardest for insertion sort is when the list is in reversed sorted order
# and in this case the while loop will execute and also have to perform maximum number swaps.
def insertion_sort(input_list):
    output_list = input_list.copy()

    if len(output_list) <= 1:
        return output_list

    for i in range(1, len(output_list)):
        value = output_list[i]

        j = i - 1
        while j >= 0 and output_list[j] > value:
            output_list[j + 1] = output_list[j]
            j -= 1
        output_list[j + 1] = value

    return output_list


# Question 5
# A function like this can be used in a school situation for attendance.
def list_of_names_to_file(name_list):
    output_file = open("sorted_names.txt", "w")
    name_list = [name.lower() for name in name_list]
    name_list.sort()

    for name in name_list:
        output_file.write((name[0]).upper() + name[1:] + "\n")


# Question 6
def binary_search(num_list, num):
    lower_bound = 0
    upper_bound = len(num_list) - 1

    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound) // 2
        if num_list[middle] == num:
            return True
        elif num_list[middle] > num:
            upper_bound = middle - 1
        else:
            lower_bound = middle + 1
    return False


# Question 7
# The solution to this is not given as it is a bonus question which is meant to challenge you.
