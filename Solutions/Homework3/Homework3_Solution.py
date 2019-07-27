"""
Solutions for Homework3
Note: The docstrings will not be done in the solutions
Note2: The solutions here are not the best and is done the way
it is to make it as easy to understand as possible. Some solutions can
be a lot shorter and even more efficient.
"""

# Question 1
def question1(input_list):
    output_list = []
    for sublist in input_list:
        for num in sublist:
            output_list.append(num)
    return output_list
print("Question 1")
print(question1([[1, 2], [3, 6], [8, 99]]))


# Question 2
def question2(input_list):
    # First compare the first and second sublist
    list1 = input_list[0]
    list2 = input_list[1]
    for num in list1:
        if num in list2:
            print("There are duplicates between the first and second sublist")
            break

    # Now compare the first and third sublist
    list1 = input_list[0]
    list2 = input_list[2]
    for num in list1:
        if num in list2:
            print("There are duplicates between the first and third sublist")
            break

    # Finally compare the second and third sublist
    list1 = input_list[1]
    list2 = input_list[2]
    for num in list1:
        if num in list2:
            print("There are duplicates between the second and third sublist")
            break
print("Question 2")
question2([[1, 4, 5], [5, 1, 7], [0, 99, 100]])


# Question 3
def question3(input_list):
    output_list = []
    for i in range(0, len(input_list), 4):
        output_list.append(input_list[i:i + 4])
    return output_list
print("Question 3")
print(question3([i for i in range(20)]))


# Question 4
def question4():
    output_data = [[[], []], [[], []]]
    for i in range(10):
        user_input = input("Enter day, name and age: ")
        user_input_split = user_input.split(",")
        if user_input[0].lower() == "monday":
            if int(user_input[2]) >= 18:
                output_data[0][0].append(user_input)
            else:
                output_data[0][1].append(user_input)
        elif user_input[0].lower() == "friday":
            if int(user_input[2]) >= 18:
                output_data[1][0].append(user_input)
            else:
                output_data[1][1].append(user_input)
    return output_data


# Question 5
def question5(input_list):
    num_of_sublist = len(input_list)
    for sublist in input_list:
        if len(sublist) != num_of_sublist:
            return False
    # If we are able to get here without returning False during the for loop
    # then that means the list is square
    return True


# Question 6
def question6(height):
    # First lets figure out how long the base of the triangle will be
    # You need to find a pattern between the base length and height of triangle (easy math -- Linear questions)
    base_length = ((height - 1) * 2) + 1
    num_of_stars = 1  # Use this to help determine how many stars ti draw per level

    # Now we can easily draw the triangle
    for level in range(height):
        num_of_spaces = base_length - num_of_stars
        print((" " * (num_of_spaces//2)) + ("*" * num_of_stars) + (" " * (num_of_spaces//2)))
        num_of_stars += 2
print("Question 6")
question6(5)


# Question 7
def question7(height):
    if height < 4:
        return  # We just get out and do nothing

    # The height meets the requirement so now we draw the letter P
    # First lets draw the head which is the same regardless of height
    print("*" * 5)
    print("*" + (" " * 3) + "*")
    print("*" * 5)

    # Finally we draw the straight part we depends on the height
    print("*\n" * (height - 3))
print("Question 7")
question7(7)