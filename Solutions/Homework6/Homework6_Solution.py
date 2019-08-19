"""
The following are solutions for homework 6
"""


# Question 1
"""
Insertion sort
start [2, 5, 1, 4, 3, 7, 10, 0]
      [2, 5, 1, 4, 3, 7, 10, 0]
      [1, 2, 5, 4, 3, 7, 10, 0]
      [1, 2, 4, 5, 3, 7, 10, 0]
      [1, 2, 3, 4, 5, 7, 10, 0]
      [1, 2, 3, 4, 5, 7, 10, 0]
      [1, 2, 3, 4, 5, 7, 10, 0]
end   [0, 1, 2, 3, 4, 5, 7, 10]

Bubble sort
start [2, 5, 1, 4, 3, 7, 10, 0]
      [2, 1, 4, 3, 5, 7, 0, 10]
      [1, 2, 3, 4, 5, 0, 7, 10]
      [1, 2, 3, 4, 0, 5, 7, 10]
      [1, 2, 3, 0, 4, 5, 7, 10]
      [1, 2, 0, 3, 4, 5, 7, 10]
      [1, 0, 2, 3, 4, 5, 7, 10]
      [0, 1, 2, 3, 4, 5, 7, 10]
end   [0, 1, 2, 3, 4, 5, 7, 10]
"""


# Question 2
"""
There are no restrictions insertion sort. You can use this to sort any type of list. Insertion sort will always work
if implemented properly. The reason if because the code is not dependent on any preconditions now maybe you have not 
seen the code yet fine. The algorithm does not depend on any preconditions. You should at least know and understand
the algorithm.
"""


# Question 3
"""
Solution will not be given for challenge questions. You need to think.
"""


# Question 4
"""
Linear search will work on all cases as we are manually going through each element. Binary search will only work
if the list given is already sorted. 
"""


# Question 5
def binary_search(list_of_nums, target_num):
    lower_bound = 0
    upper_bound = len(list_of_nums)

    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound) // 2
        if list_of_nums[middle] == target_num:
            return True
        elif list_of_nums[middle] > target_num:
            upper_bound -= 1
        else:
            lower_bound += 1
    return False


# Question 6
"""
Solution will not be provided for challenge questions
"""