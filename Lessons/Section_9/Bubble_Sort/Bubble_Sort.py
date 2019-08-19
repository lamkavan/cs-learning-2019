"""
In this section we talk about a basic sorting algorithm that any computer scientist would know about.
This would be bubble sort. Why it is called bubble sort I am not really sure, but the name is not so important.
We begin with the algorithm then move over to the code. After, we will discuss why this is generally not a very good
solution for sorting.

The algorithm...
1) We will loop over the entire input list n times where n is the len of the input list
2) Each time we loop over the entire input list we go through all the numbers from left to right, but
   we stop at after the second last value.
3) For every value we look at we check the value in directly in front and if the value in front is
   bigger we swap the two values. The reason why we stop at the second last value in 2) is because
   we always look at the value in front and the last value in the list does not have a value in front

Below is the code. There are two versions. The first is just the basic code to implement the algorithm
and the second version is the same thing but with extra output to help users see how the list changes
after each iteration.
"""
def bubble_sort(input_list):
    return_list = input_list.copy()

    for x in range(0, len(input_list)):
        for y in range(0, len(input_list) - 1):
            if (return_list[y] > return_list[y + 1]):
                temp = return_list[y]
                return_list[y] = return_list[y + 1]
                return_list[y + 1] = temp

    return return_list


def bubble_sort_with_steps(input_list):
    return_list = input_list.copy()

    print("Initial state: " + str(return_list))
    for x in range(0, len(input_list)):
        for y in range(0, len(input_list) - 1):
            if (return_list[y] > return_list[y + 1]):
                temp = return_list[y]
                return_list[y] = return_list[y + 1]
                return_list[y + 1] = temp
        print("State after " + str(x + 1) + "iterations: " + str(return_list))

    return return_list


"""
So now that you know what bubble sort is. Lets talk about why this particular algorithm is not the best. As you have
noticed, this algorithm makes a lot of comparison. In fact, if the input list had length n then the algorithm is making
n comparisons for each outer iteration. The outer for loop does n iterations and n comparisons are made during each of 
those iterations. This results in n * n or n^2 comparisons in total. This is a a lot of comparisons and the number
of comparisons we make grows quadratically as the inout list gets bigger. Of course there are tricks to make bubble sort
run faster but that would be not the traditional/simple bubble sort that I want you to learn. It turns out there are
better sorting algorithms and you will learn these as you progress through you computer science career. 
"""
