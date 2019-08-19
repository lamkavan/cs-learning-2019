"""
Linear search is the most basic search algorithm that anyone can use and implement.
This is most likely something you have already programmed, but just never knew it was
called linear search. In this section we will go through the simple algorithm and
explain why it is called linear search.

The algorithm is as follows...
Note: We are assuming that we are searching a one dimensional list of numbers for simplicity
1) Start searching at the beginning of the list and move from left to right
2) Check if each number we encounter in the list is the one we are looking for
3) If we have found the number then return True
4) If we went through the whole list without finding the number then return False

The code...
"""
def linear_search(list_of_nums, target_num):
    for num in list_of_nums:
        if num == target_num:
            return True
    return False

"""
So as you can see it is quite simple and you probably seen or done this yourself before.
The reason why it is called linear search is because you are going through the list from
left to right in a straight line. Key word straight.
"""